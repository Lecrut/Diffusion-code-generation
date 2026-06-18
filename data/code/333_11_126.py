class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start_index = None
        for i in range(len(text)):
            char = text[i]
            is_alpha_numeric_or_underscore = ('a' <= char.lower() <= 'z') or \
                                              ('0' <= char.upper() <= '9') or \
                                              char == '_'
            if not current_word_start_index:
                if is_alpha_numeric_or_underscore and (i > 0 or text[i-1] != " ") and i < len(text):
                    words.append(char)
                    current_word_start_index = True
            elif char == ' ':
                pass
        return "".join(words)
    def get_first_chars_optimized(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        result = []
        in_word = False
        for char in text:
            is_alpha_numeric_or_underscore = ('a' <= char.lower() <= 'z') or \
                                              ('0' <= char.upper() <= '9') or \
                                              char == '_'
            if not in_word and (is_alpha_numeric_or_underscore):
                result.append(char)
                in_word = True
        return "".join(result)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python 3.10 is great!",
        "_private_variable_ and public_var",
        "",
        "   ",
        "SingleWord"
    ]
    for case in test_cases:
        output = processor.get_first_chars_optimized(case)
        print(f'Input: "{case}" -> Output: "{output}"')