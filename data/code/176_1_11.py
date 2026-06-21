import re

class UniqueWordExtractor:
    def __init__(self):
        self.word_set = set()
        self.word_list = []

    def extract_unique_words(self, text):
        words = re.findall(r'[a-zA-Z]+', text)
        for word in words:
            lower_word = word.lower()
            if lower_word not in self.word_set:
                self.word_set.add(lower_word)
                self.word_list.append(lower_word)

    def get_unique_words(self):
        return self.word_list

if __name__ == '__main__':
    extractor = UniqueWordExtractor()
    sample_string = "Hello World! This is a test string with numbers 123 and punctuation."
    extractor.extract_unique_words(sample_string)
    print(extractor.get_unique_words())