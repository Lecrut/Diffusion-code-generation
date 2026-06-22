class CharacterFrequency:
    def __init__(self):
        self.frequency = {}

    def count_characters(self, phrase):
        for char in phrase.lower():
            if char.isalpha():
                self.frequency[char] = self.frequency.get(char, 0) + 1

    def get_duplicates(self):
        return {char: count for char, count in self.frequency.items() if count > 1}

if __name__ == '__main__':
    extractor = CharacterFrequency()
    sample_phrase = "Hello world! This is a test sentence, with punctuation."
    extractor.count_characters(sample_phrase)
    duplicates = extractor.get_duplicates()
    print(duplicates)