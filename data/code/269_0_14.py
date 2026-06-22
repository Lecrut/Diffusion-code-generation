import re

class PunctuationIsolator:
    def isolate_punctuation(self, text):
        return re.sub(r'([^\w\s])', r'\1 ', text)

if __name__ == '__main__':
    isolator = PunctuationIsolator()
    sample_text = "Hello, world! How are you?"
    result = isolator.isolate_punctuation(sample_text)
    print(result)