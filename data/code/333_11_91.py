class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start = False
        for char in text:
            is_space = (char.isspace() and char != '\n')
            if is_space:
                continue
            if not current_word_start:
                words.append(char)
                current_word_start = True
        return "".join(words)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python 3.12 is awesome!",
        "",
        "   Leading spaces ",
        "SingleWord",
        "A B C D E"
    ]
    for case in test_cases:
        result = processor.get_first_chars(case)
        print(f'Input: "{case}" -> Output: "{result}"')