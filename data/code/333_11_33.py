class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start_index = None
        for i in range(len(text)):
            char = text[i]
            is_space = char.isspace()
            prev_is_space = False
            if not is_space:
                if current_word_start_index is None and i == 0:
                    current_word_start_index = i
                elif is_space:
                    pass
                if prev_is_space or (i > 0 and text[i-1].isspace()):
                    current_word_start_index = i
            else:
                is_space = True
        result_chars = []
        for i in range(len(text)):
            char = text[i]
            if not char.isspace():
                prev_char_was_space_or_start_of_string = False
                if i == 0:
                    prev_char_was_space_or_start_of_string = True
                elif i > 0 and text[i-1].isspace():
                    prev_char_was_space_or_start_of_string = True
                if not prev_char_was_space_or_start_of_string:
                    continue
                result_chars.append(char)
        return "".join(result_chars)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "  Python   Programming ",
        "One two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty",
        "",
        "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    ]
    for test_input in test_cases:
        output = processor.get_first_chars(test_input)
        print(f'Input: "{test_input}" -> Output: "{output}"')