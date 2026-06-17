class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start_index = None
        for index in range(len(text)):
            char = text[index]
            if not any(c.isspace() for c in text[:index+1]):
                words.append(char)
        return "".join(words)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python Programming is Fun",
        "   Leading spaces  ",
        "",
        "SingleWord",
        "A B C D E"
    ]
    for case in test_cases:
        result = processor.get_first_chars(case)
        print(f'Input: "{case}" -> Output: "{result}"')