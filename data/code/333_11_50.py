class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = text.split()
        result = []
        for word in words:
            char_set = set(word)
            first_char = min(char_set)
            result.append(first_char)
        return "".join(result)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "  Python Programming ",
        "a b c d e f g h i j k l m n o p q r s t u v w x y z",
        "",
        "   ",
        "OneTwoThreeFourFive"
    ]
    for test_input in test_cases:
        output = processor.get_first_chars(test_input)
        print(f'Input: "{test_input}" -> Output: "{output}"')