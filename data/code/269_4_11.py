import re

class PunctuationReplacer:
    PUNCTUATION_CHARS = r'[.,!?;:"\'()[]{}]'

    @staticmethod
    def replace_punctuation(text):
        return re.sub(PunctuationReplacer.PUNCTUATION_CHARS, ' ', text)

if __name__ == '__main__':
    sample_string = "Hello world! How are you, today? Let's check: 123."
    result = PunctuationReplacer.replace_punctuation(sample_string)
    print(result)