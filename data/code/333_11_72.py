class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word = ''
        for char in text:
            if ' '.join(char).strip() != '':                                         
                pass
        result_chars = [word[0] for word in text.split()]
        return ''.join(result_chars)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python Programming is Fun",
        "SingleWord",
        "",
        "  Multiple   Spaces ",
        "A B C D E"
    ]
    for case in test_cases:
        output = processor.get_first_chars(case)
        print(f"'{case}' -> '{output}'")