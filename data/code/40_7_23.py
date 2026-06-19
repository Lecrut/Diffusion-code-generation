class StringProcessor:

    def find_first_word_initial(self, text: str) -> str:
        if not text:
            return ''
        for char in text:
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                return char
        return ''
if __name__ == '__main__':
    processor = StringProcessor()
    sample_string_1 = 'Hello world, this is a test.'
    sample_string_2 = '   \t\nStart here.'
    sample_string_3 = '123numbers'
    sample_string_4 = '!@#$%^&*()'
    print(processor.find_first_word_initial(sample_string_1))
    print(processor.find_first_word_initial(sample_string_2))
    print(processor.find_first_word_initial(sample_string_3))
    print(processor.find_first_word_initial(sample_string_4))