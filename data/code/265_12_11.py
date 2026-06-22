class UniqueCharExtractor:
    def extract(self, text):
        seen = set()
        unique_chars = ""
        for char in text:
            if char not in seen:
                seen.add(char)
                unique_chars += char
        return unique_chars

if __name__ == '__main__':
    extractor = UniqueCharExtractor()
    sample_text1 = "Hello World"
    sample_text2 = "Programming is fun"
    sample_text3 = "AEIOUaeiou 123"
    result1 = extractor.extract(sample_text1)
    result2 = extractor.extract(sample_text2)
    result3 = extractor.extract(sample_text3)
    print(f"'{sample_text1}' -> '{result1}'")
    print(f"'{sample_text2}' -> '{result2}'")
    print(f"'{sample_text3}' -> '{result3}'")