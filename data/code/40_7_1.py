class StringProcessor:
    def find_first_word_initial(self, text: str) -> str:
        if not text:
            return ""
        first_char_index = -1
        for i, char in enumerate(text):
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                first_char_index = i
                break
        if first_char_index != -1:
            return text[first_char_index]
        else:
            return ""
if __name__ == '__main__':
    processor = StringProcessor()
    sample_string_1 = "Hello world, this is a test."
    sample_string_2 = "  \t leading spaces and multiple words"
    sample_string_3 = "singleword"
    sample_string_4 = ""
    sample_string_5 = "123numbers"
    result_1 = processor.find_first_word_initial(sample_string_1)
    result_2 = processor.find_first_word_initial(sample_string_2)
    result_3 = processor.find_first_word_initial(sample_string_3)
    result_4 = processor.find_first_word_initial(sample_string_4)
    result_5 = processor.find_first_word_initial(sample_string_5)
    print(f"'{sample_string_1}' -> {result_1}")
    print(f"'{sample_string_2}' -> {result_2}")
    print(f"'{sample_string_3}' -> {result_3}")
    print(f"'{sample_string_4}' -> {result_4}")
    print(f"'{sample_string_5}' -> {result_5}")