class WordExtractor:
    def extract_first_word(self, text: str) -> str:
        if not text or text.isspace():
            return ""
        words = text.split()
        if words:
            return words[0]
        else:
            return ""
if __name__ == '__main__':
    extractor = WordExtractor()
    sample1 = "Hello world, this is a test."
    sample2 = "   leading spaces and multiple words. "
    sample3 = "singleword"
    sample4 = ""
    sample5 = "   "
    print(f"Input: '{sample1}' -> Output: '{extractor.extract_first_word(sample1)}'")
    print(f"Input: '{sample2}' -> Output: '{extractor.extract_first_word(sample2)}'")
    print(f"Input: '{sample3}' -> Output: '{extractor.extract_first_word(sample3)}'")
    print(f"Input: '{sample4}' -> Output: '{extractor.extract_first_word(sample4)}'")
    print(f"Input: '{sample5}' -> Output: '{extractor.extract_first_word(sample5)}'")