class StringProcessor:
    def get_first_chars(self, text: str) -> str:
        if not isinstance(text, str):
            return ""
        words = []
        current_word = []
        for char in text.lower():
            if 'a' <= char <= 'z':
                current_word.append(char)
            elif current_word and (char.isspace() or char == '\n'):
                if len(current_word) > 0:
                    words.append(''.join(current_word))
                    current_word = []
        if len(current_word) > 0:
            words.append(''.join(current_word))
        return ''.join(word[0] for word in words)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python Programming Is Fun",
        "   Leading spaces  ",
        "",
        "SingleWord"
    ]
    for case in test_cases:
        result = processor.get_first_chars(case)
        print(f'Input: "{case}" -> Output: "{result}"')