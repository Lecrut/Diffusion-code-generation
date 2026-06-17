class StringProcessor:
    def get_first_chars(self, text):
        result = []
        if not text.strip():
            return ""
        prev_space = False
        for char in text:
            is_space = (char == ' ') or (ord(char) > 32 and ord(char) < 48)
            if is_space != prev_space:
                result.append(char)
                prev_space = is_space
        return ''.join(result)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python Programming 101",
        "   Leading spaces here ",
        "",
        "SingleWord"
    ]
    for case in test_cases:
        output = processor.get_first_chars(case)
        print(f'Input: "{case}" -> Output: "{output}"')