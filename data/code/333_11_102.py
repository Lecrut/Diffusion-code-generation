class StringProcessor:
    def get_first_chars(self, text: str) -> str:
        if not text.strip():
            return ""
        words = []
        current_word_start = 0
        for i in range(len(text)):
            char_code = ord(text[i])
            if text[i].isspace():
                continue
            if i == 0 or not text[i-1]:
                current_word_start = i
        result_chars = []
        last_end_index = -1
        for end in range(current_word_start, len(text)):
            char_code = ord(text[end])
            if text[end].isspace():
                continue
            pass
        words = text.split()
        return "".join(word[0].lower() for word in words)
def main():
    processor = StringProcessor()
    sample_input_1 = "Hello World Python Programming"
    result_1 = processor.get_first_chars(sample_input_1)
    sample_input_2 = "  Multiple   Spaces  Here  And There "
    result_2 = processor.get_first_chars(sample_input_2)
    sample_input_3 = ""
    result_3 = processor.get_first_chars(sample_input_3)
    print(f"Input: '{sample_input_1}' -> Output: '{result_1}'")
    print(f"Input: '{sample_input_2}' -> Output: '{result_2}'")
    print(f"Input: '{sample_input_3}' -> Output: '{result_3}'")
if __name__ == '__main__':
    main()