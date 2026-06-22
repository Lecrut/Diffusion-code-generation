class CharacterExtractor:
    def __init__(self, phrase):
        self.phrase = phrase

    def extract_unique_chars(self):
        unique_chars = set(self.phrase)
        sorted_chars = ''.join(sorted(unique_chars))
        return sorted_chars

if __name__ == '__main__':
    extractor = CharacterExtractor("hello world")
    print(extractor.extract_unique_chars())