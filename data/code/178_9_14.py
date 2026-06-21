import numpy as np

class TextProcessor:
    def __init__(self):
        self.separator = " "

    @staticmethod
    def split_and_deduplicate(text, separator=" "):
        words_with_case = text.split(separator)
        words_lowercase = [word.lower() for word in words_with_case]
        unique_words = sorted(set(words_lowercase))
        return unique_words

if __name__ == '__main__':
    sample_text = "Hello World this is a test string with repeated words and MIXED CASES"
    processor = TextProcessor()
    result = processor.split_and_deduplicate(sample_text)
    print("Unique words:", result)