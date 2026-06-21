import re

def extract_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return set(re.findall(email_pattern, text))

if __name__ == '__main__':
    sample_text = "Reach out to us at help@example.net or feedback@sample.co.uk for support."
    emails = extract_emails(sample_text)
    print(emails)