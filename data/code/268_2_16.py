class WordExtractor:
    @staticmethod
    def extract_first_word(text: str) -> str:
        words = text.split()
        return words[0] if words else ""

if __name__ == '__main__':
    extractor = WordExtractor()
    sample_string_1 = "Hello world, this is a test."
    sample_string_2 = "singleword"
    sample_string_3 = "   leading spaces and multiple words "
    sample_string_4 = ""
    sample_string_5 = "  "
    result_1 = extractor.extract_first_word(sample_string_1)
    result_2 = extractor.extract_first_word(sample_string_2)
    print(f"Input: '{sample_string_1}' -> Output: '{result_1}'")
    print(f"Input: '{sample_string_2}' -> Output: '{result_2}'")