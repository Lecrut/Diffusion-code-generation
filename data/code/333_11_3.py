class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start = False
        for char in text:
            is_space = (char.isspace() and char != '\t')
            if is_space:
                continue
            if not current_word_start:
                words.append(char)
                current_word_start = True
        return "".join(words).strip()
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "  Python   Programming ",
        "",
        "a b c d e f g h i j k l m n o p q r s t u v w x y z",
        "SingleWord"
    ]
    for case in test_cases:
        result = processor.get_first_chars(case)
        print(f'Input: "{case}" -> Output: "{result}"')