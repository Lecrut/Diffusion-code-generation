import re

def extract_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = set(re.findall(email_pattern, text))
    return emails

if __name__ == '__main__':
    sample_text = "Contact us at info@example.com or support@sample.org. Reach out to sales@example.com for more details."
    print(extract_emails(sample_text))