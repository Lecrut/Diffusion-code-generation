import string

class PunctuationIsolator:
    PUNCTUATION_CHARS = set(string.punctuation)
    
    @staticmethod
    def isolate(text):
        return [char for char in text if char in PunctuationIsolator.PUNCTUATION_CHARS]

if __name__ == '__main__':
    isolator = PunctuationIsolator()
    sample_text = "Hello, world! How are you?"
    print(isolator.isolate(sample_text))