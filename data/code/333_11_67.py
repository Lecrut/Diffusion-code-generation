class StringProcessor:
    def get_first_chars(self, text):
        result = []
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = text.split()
        for word in words:
            if word and len(word) > 1:
                result.append(word[0])
            elif not any(c.isalnum() or c == '-' for c in word):
                continue
        return "".join(result)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python is great and Java works too!",
        "",
        "   ",
        "SingleWord",
        "A B C D E"
    ]
    for case in test_cases:
        output = processor.get_first_chars(case)
        print(f'Input: "{case}" -> Output: "{output}"')