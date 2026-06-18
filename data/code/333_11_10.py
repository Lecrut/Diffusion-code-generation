class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or not text.strip():
            return ""
        result = []
        in_word = False
        for char in text.lower():
            if char.isalpha() and (not in_word):
                result.append(char)
                in_word = True
            elif char.isspace() or char == '\n' or char == '\t':
                pass
            else:
                continue
        return ''.join(result)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python Programming is Fun!",
        "",
        "   multiple   spaces   ",
        "SingleWord",
        "A B C D E"
    ]
    for case in test_cases:
        output = processor.get_first_chars(case)
        print(f'Input: "{case}" -> Output: "{output}"')