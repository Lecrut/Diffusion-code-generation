class PunctuationCounter:
    def __init__(self):
        self.punctuation_counts = {}
    
    def update_count(self, text):
        punctuation_marks = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        for char in text:
            if char in punctuation_marks:
                if char in self.punctuation_counts:
                    self.punctuation_counts[char] += 1
                else:
                    self.punctuation_counts[char] = 1
    
    def get_results(self):
        return self.punctuation_counts

if __name__ == '__main__':
    sample_string = "Hello, world! How are you? Today is 2023."
    counter = PunctuationCounter()
    counter.update_count(sample_string)
    result = counter.get_results()
    print(result)