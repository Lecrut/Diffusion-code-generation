class CharacterFrequencyExtractor:
    CHARACTERS_TO_IGNORE = set(string.punctuation + string.digits)

    @staticmethod
    def is_valid_character(char):
        return char.isalpha() and char not in CharacterFrequencyExtractor.CHARACTERS_TO_IGNORE

    @classmethod
    def extract_frequencies(cls, phrase):
        char_count = {}
        for char in phrase:
            if cls.is_valid_character(char):
                char_count[char] = char_count.get(char, 0) + 1
        return {char: count for char, count in char_count.items() if count > 1}

if __name__ == '__main__':
    extractor = CharacterFrequencyExtractor()
    sample_phrase = "Hello world! This is a test sentence."
    frequencies = extractor.extract_frequencies(sample_phrase)
    print(frequencies)