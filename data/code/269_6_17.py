class PunctuationCounter:
    def __init__(self):
        self.punctuation_marks = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        self.counts = {p: 0 for p in self.punctuation_marks}

    def count(self, text):
        for char in text:
            if char in self.punctuation_counts:
                self.counts[char] += 1
        return self.counts

if __name__ == '__main__':
    sample_string = "Hello, world! How are you? Today is 2023."
    counter = PunctuationCounter()
    result = counter.count(sample_string)
    print(result)