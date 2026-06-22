class VowelCounter:
    def __init__(self):
        self.vowels = frozenset('aeiouAEIOU')
    
    def count(self, text):
        return sum(1 for char in text if char in self.vowels)

if __name__ == '__main__':
    counter = VowelCounter()
    sample_text = "Python Programming"
    print(counter.count(sample_text))