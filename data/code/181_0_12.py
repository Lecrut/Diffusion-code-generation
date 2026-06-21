class VowelWordExtractor:
    def __init__(self):
        self.vowels = set('aeiouAEIOU')

    def extract_vowel_words(self, strings):
        return [''.join(filter(lambda char: char in self.vowels, word)) for string in strings for word in string.split()]

if __name__ == '__main__':
    extractor = VowelWordExtractor()
    sample_strings = ["Hello world", "Python programming", "Data science"]
    result = extractor.extract_vowel_words(sample_strings)
    print(result)