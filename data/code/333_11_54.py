class StringProcessor:
    def get_first_chars(self, text):
        result = []
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = text.split()
        for word in words:
            if word and (word[0].isalpha()):
                result.append(word[0])
            elif word and not word[0].isalpha():
                result.append(word[0])
        return "".join(result)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python Programming is Fun",
        "   Leading spaces  ",
        "",
        "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    ]
    for test_input in test_cases:
        output = processor.get_first_chars(test_input)
        print(f'Input: "{test_input}" -> Output: "{output}"')