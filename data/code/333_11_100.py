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
                if is_alpha_numeric_or_underscore and (i + 1 >= len(text) or text[i+1] != " ") and i > 0:
                    words.append(char.lower())
                    continue
                elif char == ' ':
                    current_word_start_index = None
            else:
                if is_alpha_numeric_or_underscore and i + 1 < len(text):
                    if text[i+1] == " ":
                        words.append(char.lower())
                        current_word_start_index = None
        return "".join(words).lower()
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python Programming is Fun!",
        "",
        "   Multiple Spaces Between Words  ",
        "SingleWord123"
    ]
    for case in test_cases:
        result = processor.get_first_chars(case)
        print(f'Input: "{case}" -> Output: "{result}"')