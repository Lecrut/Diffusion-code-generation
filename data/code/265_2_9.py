class UniqueCharacterExtractor:

    def extract_non_repeated_chars(self, phrase):
        char_count = {}
        non_repeated_chars = []
        for char in phrase:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        for char, count in char_count.items():
            if count == 1:
                non_repeated_chars.append(char)
        return ''.join(non_repeated_chars)
if __name__ == '__main__':
    extractor = UniqueCharacterExtractor()
    sample_phrase = 'Hello World! 123'
    result = extractor.extract_non_repeated_chars(sample_phrase)
    print(result)