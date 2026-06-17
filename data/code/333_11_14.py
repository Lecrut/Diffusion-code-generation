class StringProcessor:
    def get_first_chars(self, s: str) -> str:
        if not s.strip():
            return ""
        words = s.split()
        result_parts = [word[0] for word in words]
        return "".join(result_parts)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python 3.12 Is Amazing",
        "   Leading Spaces ",
        "",
        "SingleWord"
    ]
    for case in test_cases:
        output = processor.get_first_chars(case)
        print(f'Input: "{case}" -> Output: "{output}"')