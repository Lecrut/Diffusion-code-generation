class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start_index = None
        for i in range(len(text)):
            char = text[i]
            is_alpha_numeric_or_underscore = ('a' <= char.lower() <= 'z') or \
                                              ('0' <= char <= '9') or \
                                              char == '_'
            if not current_word_start_index:
                if is_alpha_numeric_or_underscore and (i > 0 or text[i-1] != " ") and i < len(text):
                    words.append(char)
                    current_word_start_index = True
            elif char == ' ':
                pass
        return "".join(words)
    def get_first_chars_optimized(self, text):
        result = []
        prev_char_is_space_or_empty = True
        for char in text:
            is_alpha_numeric_or_underscore = ('a' <= char.lower() <= 'z') or \
                                            ('0' <= char <= '9') or \
                                            char == '_'
            if not prev_char_is_space_or_empty and (is_alpha_numeric_or_underscore):
                result.append(char)
        return "".join(result)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python 3.10 is great!",
        "_test_case_123",
        "",
        "   multiple   spaces   here   ",
        "SingleWord"
    ]
    for case in test_cases:
        output = processor.get_first_chars_optimized(case)
        print(f'Input: "{case}" -> Output: "{output}"')