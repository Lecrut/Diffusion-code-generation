class VowelCounter:
    def __init__(self):
        self.vowels = frozenset('aeiouAEIOU')

    def count(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return sum(1 for char in text if char in self.vowels)

if __name__ == '__main__':
    counter = VowelCounter()
    sample_text = "A quick brown fox jumps over the lazy dog"
    print(counter.count(sample_text))