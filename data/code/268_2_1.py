class WordExtractor:
    def extract_first_word(self, text: str) -> str:
        if not text:
            return ""
        words = text.split()
        if words:
            return words[0]
        else:
            return ""
if __name__ == '__main__':
    extractor = WordExtractor()
    sample_string_1 = "This is a sample sentence."
    sample_string_2 = "another test string here"
    sample_string_3 = "singleword"
    sample_string_4 = ""
    sample_string_5 = "   leading spaces and multiple words"
    result_1 = extractor.extract_first_word(sample_string_1)
    result_2 = extractor.extract_first_word(sample_string_2)
    result_3 = extractor.extract_first_word(sample_string_3)
    result_4 = extractor.extract_first_word(sample_string_4)
    result_5 = extractor.extract_first_word(sample_string_5)
    print(f"Input: '{sample_string_1}' -> Output: '{result_1}'")
    print(f"Input: '{sample_string_2}' -> Output: '{result_2}'")
    print(f"Input: '{sample_string_3}' -> Output: '{result_3}'")
    print(f"Input: '{sample_string_4}' -> Output: '{result_4}'")
    print(f"Input: '{sample_string_5}' -> Output: '{result_5}'")