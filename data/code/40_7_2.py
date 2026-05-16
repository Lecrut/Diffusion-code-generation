class StringProcessor:
    def find_first_word_initial(self, text: str) -> str:
        if not text:
            return ""
        first_char = None
        for char in text:
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                first_char = char
                break
        return first_char if first_char is not None else ""
if __name__ == '__main__':
    processor = StringProcessor()
    sample1 = "Hello world, this is a test."
    sample2 = "  leading spaces and multiple words"
    sample3 = "123numbersonly"
    sample4 = ""
    sample5 = "   "
    print(f"'{sample1}' -> {processor.find_first_word_initial(sample1)}")
    print(f"'{sample2}' -> {processor.find_first_word_initial(sample2)}")
    print(f"'{sample3}' -> {processor.find_first_word_initial(sample3)}")
    print(f"'{sample4}' -> {processor.find_first_word_initial(sample4)}")
    print(f"'{sample5}' -> {processor.find_first_word_initial(sample5)}")