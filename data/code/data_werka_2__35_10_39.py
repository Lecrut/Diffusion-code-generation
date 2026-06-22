class VowelCounter:
    VOWELS = set('aeiouAEIOU')

    @staticmethod
    def is_vowel(char):
        return char in VowelCounter.VOWELS

    def count(self, text):
        return sum(VowelCounter.is_vowel(char) for char in text)

if __name__ == '__main__':
    counter = VowelCounter()
    sample_text = "The quick brown fox jumps over the lazy dog"
    print(counter.count(sample_text))