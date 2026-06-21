import re

def extract_emails(text):
    pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', re.IGNORECASE)
    return pattern.findall(text)

if __name__ == '__main__':
    sample_text = "For questions, reach out to info@example.net or feedback@example.co.uk."
    emails = extract_emails(sample_text)
    print(emails)