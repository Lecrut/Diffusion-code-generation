class UniqueCharExtractor:
    @staticmethod
    def extract_unique_chars(phrase):
        unique_chars = set(phrase)
        sorted_chars = ''.join(sorted(unique_chars))
        return sorted_chars

if __name__ == '__main__':
    sample_phrase = "hello world"
    extractor = UniqueCharExtractor()
    result = extractor.extract_unique_chars(sample_phrase)
    print(result)