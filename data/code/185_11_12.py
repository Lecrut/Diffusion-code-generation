import re

class EmailExtractor:
    def __init__(self):
        self.email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    def extract_emails(self, text):
        return set(re.findall(self.email_pattern, text))

if __name__ == '__main__':
    extractor = EmailExtractor()
    sample_text = "Please contact us at support@example.com or sales@example.org for further inquiries. Thank you!"
    emails = extractor.extract_emails(sample_text)
    print(emails)