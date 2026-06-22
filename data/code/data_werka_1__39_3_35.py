import re

def extract_words(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    try:
        words = re.findall(r'\b\w+\b', input_string)
        return words
    except TypeError as e:
        raise RuntimeError("Failed to extract words") from e

class WordExtractor:
    def __init__(self, input_string):
        self.input_string = input_string
    
    def get_words(self):
        return extract_words(self.input_string)

if __name__ == '__main__':
    sample_input = """Hello, world! This is a test string with multiple words,
    including numbers like 123 and special characters #@$%^&*()."""
    
    extractor = WordExtractor(sample_input)
    extracted_words = extractor.get_words()
    print(extracted_words)