class ConsonantCounter:
    def __init__(self):
        self.vowels = set('aeiouAEIOU')

    def is_consonant(self, char):
        return char.isalpha() and char not in self.vowels

    def count_consonants(self, text):
        return sum(1 for char in text if self.is_consonant(char))

    def count_vowels(self, text):
        return sum(1 for char in text if char in self.vowels)

    def count_alpha(self, text):
        return sum(1 for char in text if char.isalpha())

if __name__ == '__main__':
    counter = ConsonantCounter()
    sample = "Hello World 123"
    print(counter.count_consonants(sample))
    print(counter.count_vowels(sample))
    print(counter.count_alpha(sample))