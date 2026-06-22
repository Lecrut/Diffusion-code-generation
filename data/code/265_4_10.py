class VowelExtractor:
    VOWELS = "aeiouAEIOU"

    @staticmethod
    def extract_vowels_reversed(phrase):
        return ''.join(filter(lambda char: char in VowelExtractor.VOWELS, phrase))[::-1]

if __name__ == '__main__':
    sample_phrase = "Programming is fun!"
    reversed_vowels = VowelExtractor.extract_vowels_reversed(sample_phrase)
    print(reversed_vowels)