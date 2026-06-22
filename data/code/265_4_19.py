class VowelExtractor:
    VOWELS = "aeiouAEIOU"

    @staticmethod
    def extract_vowels_reverse(phrase):
        vowels = [char for char in phrase if char in VowelExtractor.VOWELS]
        return ''.join(vowels[::-1])

if __name__ == '__main__':
    sample_phrase = "Hello World!"
    result = VowelExtractor.extract_vowels_reverse(sample_phrase)
    print(result)