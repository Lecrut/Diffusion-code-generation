import string

class PunctuationCounter:
    def __init__(self):
        self.punctuation_count = {}

    def count_punctuation(self, text):
        for char in text:
            if char in string.punctuation:
                self.punctuation_count[char] = self.punctuation_count.get(char, 0) + 1

    def get_punctuation_count(self):
        return self.punctuation_count

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test. It contains various punctuation marks:.,;:'\"!?()[]{}@#$%^&*-_+=|\\/<>"
    counter = PunctuationCounter()
    counter.count_punctuation(sample_text)
    print(counter.get_punctuation_count())