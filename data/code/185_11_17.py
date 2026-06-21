import re

def is_valid_email(email):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return bool(re.match(email_pattern, email))

def extract_emails(text):
    emails = set()
    words = text.split()
    for word in words:
        if is_valid_email(word):
            emails.add(word)
    return emails

if __name__ == '__main__':
    sample_text = "Please contact us at support@example.com or sales@example.org. Thank you!"
    print(extract_emails(sample_text))