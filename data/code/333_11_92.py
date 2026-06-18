class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start_index = -1
        for i in range(len(text)):
            char_code = ord(text[i])
            if 'A' <= text[i] <= 'Z':
                pass                                                                                                     
        words = [word.strip() for word in text.split()] if text else []
        result_chars = [w[0] for w in words if len(w) > 0]
        return ''.join(result_chars)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python Programming is Fun",
        "",
        "   Multiple   Spaces   Here  ",
        "SingleWord"
    ]
    for case in test_cases:
        output = processor.get_first_chars(case)
        print(f'Input: "{case}" -> Output: "{output}"')