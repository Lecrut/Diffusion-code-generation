import re

class TextProcessor:
    def __init__(self):
        self.pattern = r'[a-zA-Z]+'

    def extract_words(self, text):
        return re.findall(self.pattern, text)

if __name__ == '__main__':
    processor = TextProcessor()
    sample_string1 = "Hello world! This is a test sentence with various spaces."
    sample_string2 = "  leading space and trailing spaces   \t\nmultiple\tspaces here. "
    sample_string3 = "123 numbers and symbols @#$"
    
    result1 = processor.extract_words(sample_string1)
    print(f"Input: '{sample_string1}'")
    print(f"Output: {result1}")
    print("-" * 20)
    
    result2 = processor.extract_words(sample_string2)
    print(f"Input: '{sample_string2.replace('\n', ' ').replace('\t', '  ')}' (normalized for display)")
    print(f"Output: {result2}")
    print("-" * 20)
    
    result3 = processor.extract_words(sample_string3)
    print(f"Input: '{sample_string3}'")
    print(f"Output: {result3}")