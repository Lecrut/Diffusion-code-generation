import re

EMAIL_PATTERN = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def extract_emails(text):
    return set(re.findall(EMAIL_PATTERN, text))

if __name__ == '__main__':
    sample_text = "Please contact us at support@example.com or sales@example.org for further inquiries. Thank you!"
    print(extract_emails(sample_text))