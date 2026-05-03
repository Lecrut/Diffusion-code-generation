class StringProcessor:
    def find_first_word_initial(self, text: str) -> str:
        if not text:
            return ""
        first_char = None
        for char in text:
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                first_char = char
                break
        if first_char is not None:
            return first_char
        else:
            return ""
if __name__ == '__main__':
    processor = StringProcessor()
    sample_string_1 = "Hello world, this is a test."
    sample_string_2 = "   \t\n\rStart here."
    sample_string_3 = "123numbersonly"
    sample_string_4 = ""
    sample_string_5 = "   "
    result_1 = processor.find_first_word_initial(sample_string_1)
    result_2 = processor.find_first_word_initial(sample_string_2)
    result_3 = processor.find_first_word_initial(sample_string_3)
    result_4 = processor.find_first_word_initial(sample_string_4)
    result_5 = processor.find_first_word_initial(sample_string_5)
    print(f"'{sample_string_1}' -> '{result_1}'")
    print(f"'{sample_string_2}' -> '{result_2}'")
    print(f"'{sample_string_3}' -> '{result_3}'")
    print(f"'{sample_string_4}' -> '{result_4}'")
    print(f"'{sample_string_5}' -> '{result_5}'")