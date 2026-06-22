import re

class StringProcessor:
    def remove_spaces(self, text):
        return re.sub(r'\s+', '', text)

if __name__ == '__main__':
    processor = StringProcessor()
    sample_text = "Hello, World! This is a test."
    result = processor.remove_spaces(sample_text)
    print(result)