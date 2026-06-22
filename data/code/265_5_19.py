class CharacterFrequencyExtractor:
    def __init__(self):
        self.IGNORE_CASE = True

    @staticmethod
    def is_valid_char(char):
        return char.isalpha()

    def extract_frequencies(self, phrase):
        frequency_map = {}
        for char in phrase:
            if self.is_valid_char(char):
                char = char.lower() if self.IGNORE_CASE else char
                frequency_map[char] = frequency_map.get(char, 0) + 1
        return {char: count for char, count in frequency_map.items() if count > 1}

if __name__ == '__main__':
    extractor = CharacterFrequencyExtractor()
    sample_phrase = "Hello world! This is a test sentence."
    frequencies = extractor.extract_frequencies(sample_phrase)
    print(frequencies)