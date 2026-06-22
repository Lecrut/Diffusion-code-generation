class VowelCounter:
    def count(self, text):
        vowels = set('aeiouAEIOU')
        return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    counter = VowelCounter()
    sample_text = "Hello, World!"
    print(counter.count(sample_text))