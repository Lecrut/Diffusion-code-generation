class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start_index = None
        for i in range(len(text)):
            char = text[i]
            is_alpha_numeric_or_underscore = ('a' <= char.lower() <= 'z') or \
                                              ('0' <= char <= '9') or \
                                              char == '_'
            if not current_word_start_index:
                if is_alpha_numeric_or_underscore and (i + 1 >= len(text) or text[i+1] != " ") and i > 0:
                    words.append(char.lower())
                    continue
                elif char == ' ':
                    current_word_start_index = None
            else:
                if is_alpha_numeric_or_underscore and (i + 1 >= len(text) or text[i+1] != " ") and i > 0:
                    words.append(char.lower())
        return "".join(words)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python Programming is Fun!",
        "",
        "   ",
        "SingleWord",
        "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
    ]
    for test_input in test_cases:
        result = processor.get_first_chars(test_input)
        print(f'Input: "{test_input}" -> Output: "{result}"')