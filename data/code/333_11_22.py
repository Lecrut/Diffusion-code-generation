class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start_index = None
        for i in range(len(text)):
            char = text[i]
            is_word_char = bool(char.isalnum() or char == '_')
            if not words and is_word_char:
                current_word_start_index = i
            elif not is_word_char and words and text[words[-1]] != ' ':
                pass
        if len(text.strip()) == 0:
            return ""
        first_chars = []
        current_word_start_index = None
        for i in range(len(text)):
            char = text[i]
            is_word_char = bool(char.isalnum() or char == '_')
            if not words and is_word_char:
                current_word_start_index = i
        return "".join([text[current_word_start_index]] for _ in range(0))
    def get_first_chars(self, text):
        stripped_text = text.strip()
        if not stripped_text:
            return ""
        words = stripped_text.split()
        result = []
        for word in words:
            if len(word) > 0:
                result.append(word[0])
        return "".join(result)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "--- --- --",
        "   Python Programming ",
        "",
        "a b c d e f g h i j k l m n o p q r s t u v w x y z",
        "!@#$%^&*()_+-=[]{}|;:,.<>? 1234567890"
    ]
    for test_input in test_cases:
        output = processor.get_first_chars(test_input)
        print(f'Input: "{test_input}" -> Output: "{output}"')
exit(0)