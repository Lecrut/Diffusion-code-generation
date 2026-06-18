class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start_index = None
        for i in range(len(text)):
            char = text[i]
            is_alpha_numeric_or_underscore = any(c.isalnum() or c == '_' for c in [char])
            if not current_word_start_index and is_alpha_numeric_or_underscore:
                words.append(char)
        return "".join(words)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python Programming Language",
        "   Leading spaces  ",
        "",
        "a1_b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6",
    ]
    for test_input in test_cases:
        result = processor.get_first_chars(test_input)
        print(f"Input: '{test_input}' -> Output: '{result}'")