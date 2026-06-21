import re

class WordExtractor:
    def __init__(self):
        self.pattern = r'[a-zA-Z]+'

    def extract(self, text):
        return re.findall(self.pattern, text)

if __name__ == '__main__':
    extractor = WordExtractor()
    
    sample_string1 = "Hello world! This is a test sentence with various spaces."
    sample_string2 = "  leading space and trailing spaces   \t\nmultiple\tspaces here. "
    sample_string3 = "123 numbers and symbols @#$"
    
    result1 = extractor.extract(sample_string1)
    print(f"'{sample_string1}' -> {result1}")
    
    result2 = extractor.extract(sample_string2)
    print(f"'{sample_string2.replace('\n', ' ').replace('\t', '  ')}' (normalized for display) -> {result2}")
    
    result3 = extractor.extract(sample_string3)
    print(f"'{sample_string3}' -> {result3}")