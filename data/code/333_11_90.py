class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start_index = None
        for i in range(len(text)):
            char = text[i]
            is_new_word = False
            if i == 0:
                is_new_word = True
            elif current_word_start_index is not None and text[current_word_start_index] in ' \t\n\r':
                prev_char_idx = i - 1
                if prev_char_idx >= 0:
                    if text[prev_char_idx].isspace() or not (text[current_word_start_index] == 'a' and current_word_start_index > 0):                                                                      
                        pass
        return ''.join([word[0] if word else '' for word in text.split()])
    def get_first_chars_optimized(self, text):
        result = []
        stripped_text = text.strip()
        if not stripped_text:
            return ""
        current_word_start_index = 0
        for i in range(len(stripped_text)):
            char = stripped_text[i]
            if not (char.isalpha() or char.isdigit()):
                continue
        return ''.join([word[0] for word in stripped_text.split()])
    def get_first_chars_final(self, text):
        words = text.strip().split()
        if not words:
            return ""
        first_chars = [word[0] for word in words]
        return ''.join(first_chars)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python 3.12 is awesome!",
        "   Leading spaces here ",
        "",
        "SingleWord",
        "A B C D E"
    ]
    for input_str in test_cases:
        output = processor.get_first_chars_final(input_str)
        print(f'Input: "{input_str}" -> Output: "{output}"')