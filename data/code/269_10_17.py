import string

class PunctuationIsolator:
    def __init__(self):
        self.punctuation_set = set(string.punctuation)
    
    def isolate(self, text):
        return [char for char in text if char in self.punctuation_set]

if __name__ == '__main__':
    isolator = PunctuationIsolator()
    sample_text = "Hello, world! How are you?"
    result = isolator.isolate(sample_text)
    print(result)