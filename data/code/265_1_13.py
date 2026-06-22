class UniqueCharacterExtractor:
    def __init__(self):
        self.seen_chars = set()

    @staticmethod
    def is_unique_char(char, seen_chars):
        return char not in seen_chars

    def extract_unique_characters(self, phrase):
        result = []
        for char in phrase:
            if self.is_unique_char(char, self.seen_chars):
                result.append(char)
                self.seen_chars.add(char)
        return result

if __name__ == '__main__':
    extractor = UniqueCharacterExtractor()
    sample_phrase1 = "hello world"
    print(extractor.extract_unique_characters(sample_phrase1))