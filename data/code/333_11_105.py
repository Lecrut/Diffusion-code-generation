class StringProcessor:
    def first_char_of_words(self, text: str) -> str:
        words = text.split() if text else []
        return ''.join(word[0] for word in words)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "",
        "a b c d e f g h i j k l m n o p q r s t u v w x y z",
        "  Leading spaces ",
        "Multiple   Spaces"
    ]
    for case in test_cases:
        result = processor.first_char_of_words(case)
        print(f'Input: "{case}" -> Output: "{result}"')