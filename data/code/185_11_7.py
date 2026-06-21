import re

def extract_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return set(re.findall(email_pattern, text))

if __name__ == '__main__':
    sample_text = "Contact us at info@example.com or support@sample.org. Reach out to sales@example.com for more info."
    print(extract_emails(sample_text))