import re

class WordFinder:
    def __init__(self):
        self.distinct_words = set()

    def add_word(self, word):
        if word:
            self.distinct_words.add(word)

    def find_distinct_words(self, text):
        words = re.findall(r'\b\w+\b', text.lower())
        for word in words:
            self.add_word(word)
        return self.distinct_words

if __name__ == '__main__':
    sample_string = "This is a test string with repeated words and some punctuation."
    finder = WordFinder()
    distinct_words = finder.find_distinct_words(sample_string)
    print(distinct_words)