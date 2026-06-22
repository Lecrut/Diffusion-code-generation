class ConsonantExtractor:
    VOWELS = 'aeiouAEIOU'

    @staticmethod
    def extract_non_vowels_reverse(phrase):
        non_vowel_chars = [char for char in phrase if char not in ConsonantExtractor.VOWELS]
        return ''.join(non_vowel_chars[::-1])

if __name__ == '__main__':
    extractor = ConsonantExtractor()
    sample_phrase = 'Hello, World!'
    result = extractor.extract_non_vowels_reverse(sample_phrase)
    print(result)