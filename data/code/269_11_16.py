import string

class PunctuationExtractor:
    def __init__(self):
        self.punctuation_count = {}

    def extract_and_count(self, text):
        for char in text:
            if char in string.punctuation:
                if char in self.punctuation_count:
                    self.punctuation_count[char] += 1
                else:
                    self.punctuation_count[char] = 1

if __name__ == '__main__':
    extractor = PunctuationExtractor()
    
    sample_string1 = "Hello, world! How are you?"
    extractor.extract_and_count(sample_string1)
    print(f"Punctuation in '{sample_string1}': {extractor.punctuation_count}")
    
    sample_string2 = "This is a test string with numbers 123 and symbols @#$."
    extractor.extract_and_count(sample_string2)
    print(f"Punctuation in '{sample_string2}': {extractor.punctuation_count}")
    
    sample_string3 = "No punctuation here."
    extractor.extract_and_count(sample_string3)
    print(f"Punctuation in '{sample_string3}': {extractor.punctuation_count}")