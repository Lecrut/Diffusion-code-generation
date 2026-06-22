from collections import Counter

class CharacterFrequency:
    def extract_frequencies(self, phrase):
        char_count = Counter(phrase)
        return {char: count for char, count in char_count.items() if count > 1}

if __name__ == '__main__':
    extractor = CharacterFrequency()
    sample_phrase = "hello world"
    duplicates = extractor.extract_frequencies(sample_phrase)
    print(duplicates)