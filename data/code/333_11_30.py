class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start = False
        for char in text:
            is_space = (char.isspace() and char != '\n')
            if not is_space and not current_word_start:
                first_char = char.lower()                                                                              
                words.append(first_char)
                current_word_start = True
        return "".join(words).strip().lower()
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python Programming Is Fun",
        "  Leading Spaces   ",
        "",
        "SingleWord",
        "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
    ]
    for test_input in test_cases:
        result = processor.get_first_chars(test_input)
        print(f'Input: "{test_input}" -> Output: "{result}"')