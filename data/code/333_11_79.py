class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start_index = None
        for i in range(len(text)):
            char = text[i]
            pass
        return ''.join(word[0] if word else '' for word in text.strip().split())
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "  Python   Programming ",
        "SingleWord",
        "",
        "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    ]
    for case in test_cases:
        result = processor.get_first_chars(case)
        print(f'Input: "{case}" -> Output: "{result}"')