import re

class WordFinder:
    WORD_PATTERN = re.compile(r'\b\w+\b')

    @staticmethod
    def find_distinct_words(text):
        words = WordFinder.WORD_PATTERN.findall(text.lower())
        distinct_words = set(words)
        return distinct_words

if __name__ == '__main__':
    sample_string = "This is a test string with repeated words and some punctuation."
    result = WordFinder.find_distinct_words(sample_string)
    print(result)