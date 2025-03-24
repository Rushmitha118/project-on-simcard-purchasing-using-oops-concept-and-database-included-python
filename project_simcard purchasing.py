import sqlite3
import random
import smtplib
from email.mime.text import MIMEText

def generate_phone_number():
    return str(random.randint(6000000000, 9999999999))  # Generates a random 10-digit number

def send_email(email, phone_number):
    sender_email = "your_email@gmail.com"  # Replace with your email
    sender_password = "your_email_password"  # Replace with your email password

    subject = "Your New SIM Card Phone Number"
    message = f"Hello,\n\nYour new phone number is: {phone_number}\n\nThank you!"

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)

def store_in_database(name, address, aadhar, email, phone_number):
    conn = sqlite3.connect("sim_database.db")
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS sim_users (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT,
                      address TEXT,
                      aadhar TEXT,
                      email TEXT,
                      phone_number TEXT)''')

    cursor.execute("INSERT INTO sim_users (name, address, aadhar, email, phone_number) VALUES (?, ?, ?, ?, ?)",
                   (name, address, aadhar, email, phone_number))
    
    conn.commit()
    conn.close()
    print("Data stored successfully!")

def main():
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    aadhar = input("Enter your Aadhar number: ")
    email = input("Enter your email: ")

    phone_number = generate_phone_number()
    
    store_in_database(name, address, aadhar, email, phone_number)
    send_email(email, phone_number)
    
    print(f"Your new phone number is: {phone_number}")

if __name__ == "__main__":
    main()