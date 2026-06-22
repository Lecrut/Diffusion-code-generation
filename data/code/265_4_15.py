class VowelExtractor:
    VOWELS = "aeiouAEIOU"

    @staticmethod
    def extract_vowels_and_reverse(phrase):
        vowels = [char for char in phrase if char in VowelExtractor.VOWELS]
        return ''.join(reversed(vowels))

if __name__ == '__main__':
    sample_phrase = "Programming is fun!"
    result = VowelExtractor.extract_vowels_and_reverse(sample_phrase)
    print(result)