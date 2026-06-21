import re

class EmailExtractor:
    def __init__(self):
        self.pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', re.IGNORECASE)

    def extract_emails(self, text):
        return self.pattern.findall(text)

if __name__ == '__main__':
    extractor = EmailExtractor()
    sample_text = "Please contact us at support@example.com or sales@example.org for further assistance."
    emails = extractor.extract_emails(sample_text)
    print(emails)