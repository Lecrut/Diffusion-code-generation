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
                words.append(char)
                current_word_start_index = i
            elif is_alpha_numeric_or_underscore and text[i-1] != " ":
                pass
        return "".join(words).strip()
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python 3.10 is awesome!",
        "_test_case_123",
        "",
        "   ",
        "SingleWord"
    ]
    for case in test_cases:
        result = processor.get_first_chars(case)
        print(f'Input: "{case}" -> Output: "{result}"')