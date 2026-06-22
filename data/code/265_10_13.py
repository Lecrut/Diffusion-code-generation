class UniqueCharExtractor:
    def extract_unique_chars(self, phrase):
        unique_chars = set(phrase)
        sorted_chars = ''.join(sorted(unique_chars))
        return sorted_chars

if __name__ == '__main__':
    extractor = UniqueCharExtractor()
    sample_phrase = "hello world"
    result = extractor.extract_unique_chars(sample_phrase)
    print(result)