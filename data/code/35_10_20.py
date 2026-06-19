class VowelCounter:
    def __init__(self):
        self.vowels = set('aeiouAEIOU')

    def count(self, text):
        return sum(1 for char in text if char in self.vowels)

if __name__ == '__main__':
    counter = VowelCounter()
    sample_text = "Hello, World!"
    print(counter.count(sample_text))