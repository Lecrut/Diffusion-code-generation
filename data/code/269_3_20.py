import string

class PunctuationCounter:
    def __init__(self):
        self.punctuation_count = {char: 0 for char in string.punctuation}

    def update_count(self, text):
        for char in text:
            if char in self.punctuation_count:
                self.punctuation_count[char] += 1

    def get_counts(self):
        return self.punctuation_count

if __name__ == '__main__':
    sample_text = "Hello, world! How are you? I'm fine. Thanks!"
    counter = PunctuationCounter()
    counter.update_count(sample_text)
    print(counter.get_counts())