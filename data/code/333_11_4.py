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
                if is_alpha_numeric_or_underscore and (char.isalpha()):
                    words.append(char)
                    current_word_start_index = i
            elif text[i] != ' ':
                continue
        return "".join(words)
    def get_first_chars_optimized(self, text):
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        result = []
        in_word = False
        for char in text:
            if ('a' <= char.lower() <= 'z') or \
               ('0' <= char.upper() <= '9') or \
               char == '_':
                if not in_word and char.isalpha():
                    result.append(char)
                    in_word = True
        return "".join(result)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python 3.10 is great!",
        "_private_variable_abc",
        "   Leading spaces only",
        "",
        "No words here"
    ]
    for case in test_cases:
        output = processor.get_first_chars_optimized(case)
        print(f'Input: "{case}" -> Output: "{output}"')