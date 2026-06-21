import re

def extract_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return set(emails)

if __name__ == '__main__':
    sample_text = "Please contact us at support@example.com or sales@example.co.uk. Alternatively, reach out to john.doe+test@domain.org."
    print(extract_emails(sample_text))