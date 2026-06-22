class UniqueCharExtractor:

    def extract_unique_chars(self, phrase):
        char_count = {}
        unique_chars = ''
        for char in phrase:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        for char, count in char_count.items():
            if count == 1:
                unique_chars += char
        return unique_chars
if __name__ == '__main__':
    extractor = UniqueCharExtractor()
    sample_phrase = 'Hello World! 123'
    result = extractor.extract_unique_chars(sample_phrase)
    print(result)