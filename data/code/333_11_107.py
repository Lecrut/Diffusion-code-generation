class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start_index = None
        for i in range(len(text)):
            char = text[i]
            is_new_word = False
            if not char.isspace():
                if current_word_start_index is None:
                    is_new_word = True
                    current_word_start_index = i
                elif text[current_word_start_index] == ' ':
                    words.append(text[i])
                    current_word_start_index = i
            if not char.isspace() and current_word_start_index is None:
                continue
        return "".join(words)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python Programming Is Fun",
        "   Leading spaces  ",
        "SingleWord",
        "",
        "A B C D E"
    ]
    for case in test_cases:
        result = processor.get_first_chars(case)
        print(f'Input: "{case}" -> Output: "{result}"')