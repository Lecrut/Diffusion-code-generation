import re

class StringProcessor:
    @staticmethod
    def remove_spaces(text):
        return re.sub(r'\s+', '', text)

if __name__ == '__main__':
    sample_text = "Hello, World! This is a test."
    processor = StringProcessor()
    result = processor.remove_spaces(sample_text)
    print(result)