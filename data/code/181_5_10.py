import re

class VowelExtractor:
    VOWELS = "aeiouAEIOU"
    
    @staticmethod
    def extract_vowels(phrase):
        return ''.join(char for char in re.sub(r'[^a-zA-Z]', '', phrase) if char in VowelExtractor.VOWELS)
    
    @staticmethod
    def unique_vowels(phrases):
        all_vowels = ''.join(VowelExtractor.extract_vowels(phrase) for phrase in phrases)
        return sorted(set(all_vowels))

if __name__ == '__main__':
    sample_phrases = ["Hello, world!", "Python programming is fun.", "Regular expressions are powerful."]
    unique_vowel_set = VowelExtractor.unique_vowels(sample_phrases)
    print(unique_vowel_set)