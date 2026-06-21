class VowelWordExtractor:
    VOOWELS = "aeiouAEIOU"

    @staticmethod
    def contains_vowel(word):
        return any(char in VowelWordExtractor.VOOWELS for char in word)

    @staticmethod
    def extract_vowel_words(strings):
        return [' '.join(filter(VowelWordExtractor.contains_vowel, word.split())) for string in strings]

if __name__ == '__main__':
    sample_strings = ["Hello world", "Python programming", "Data science"]
    print(VowelWordExtractor.extract_vowel_words(sample_strings))