import re

EMAIL_PATTERN = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', re.IGNORECASE)

def extract_emails(text):
    return EMAIL_PATTERN.findall(text)

if __name__ == '__main__':
    sample_text = "Please contact us at support@example.com or sales@example.org for further assistance."
    emails = extract_emails(sample_text)
    print(emails)