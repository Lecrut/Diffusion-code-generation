class WordExtractor:
    def extract_first_word(self, text: str) -> str:
        if not text:
            return ""
        first_word = text.split()[0]
        return first_word
if __name__ == '__main__':
    extractor = WordExtractor()
    sample_string_1 = "Hello world, this is a test."
    sample_string_2 = "singleword"
    sample_string_3 = ""
    sample_string_4 = "   leading spaces test"
    result_1 = extractor.extract_first_word(sample_string_1)
    result_2 = extractor.extract_first_word(sample_string_2)
    result_3 = extractor.extract_first_word(sample_string_3)
    result_4 = extractor.extract_first_word(sample_string_4)
    print(f"Input: '{sample_string_1}' -> Output: '{result_1}'")
    print(f"Input: '{sample_string_2}' -> Output: '{result_2}'")
    print(f"Input: '{sample_string_3}' -> Output: '{result_3}'")
    print(f"Input: '{sample_string_4}' -> Output: '{result_4}'")