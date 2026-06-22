import re

class PunctuationIsolator:
    PUNCTUATION_REGEX = r'([^\w\s])'

    @staticmethod
    def isolate_punctuation(text):
        return re.sub(PunctuationIsolator.PUNCTUATION_REGEX, r'\1 ', text)

if __name__ == '__main__':
    sample_text = "Hello, world! How are you?"
    print(PunctuationIsolator.isolate_punctuation(sample_text))