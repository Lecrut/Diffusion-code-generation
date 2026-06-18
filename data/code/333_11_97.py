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
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python Programming is Fun!",
        "",
        "   ",
        "SingleWord",
        "A B C D E"
    ]
    for case in test_cases:
        result = processor.get_first_chars(case)
        print(f'Input: "{case}" -> Output: "{result}"')