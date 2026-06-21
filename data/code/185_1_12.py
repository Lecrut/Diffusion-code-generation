import re

def validate_input(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    if len(text) == 0:
        raise ValueError("Input text cannot be empty")

def extract_emails(text):
    pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', re.IGNORECASE)
    return pattern.findall(text)

if __name__ == '__main__':
    sample_text = "Please contact us at support@example.com or sales@example.org for further assistance."
    validate_input(sample_text)
    emails = extract_emails(sample_text)
    print(emails)