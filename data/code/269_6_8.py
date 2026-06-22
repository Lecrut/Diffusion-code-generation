class PunctuationCounter:
    def __init__(self):
        self.punctuation_counts = {char: 0 for char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'}

    def count(self, text):
        for char in text:
            if char in self.punctuation_counts:
                self.punctuation_counts[char] += 1
        return self.punctuation_counts

if __name__ == '__main__':
    sample_string = "Hello, world! How are you? Today is 2023."
    counter = PunctuationCounter()
    result = counter.count(sample_string)
    print(result)