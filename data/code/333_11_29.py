class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start_index = None
        for i in range(len(text)):
            char = text[i]
            is_new_word = False
            if not char.isspace():
                if current_word_start_index is None:
                    current_word_start_index = i
                    is_new_word = True
                elif text[current_word_start_index] != ' ':
                    prev_char_idx = max(0, i - 1)
                    if current_word_start_index == 0:
                        is_new_word = True
                    elif text[prev_char_idx].isspace():
                        pass 
            else:
                continue
        return "".join([text[i] for i, char in enumerate(text) if not char.isspace() and (i == 0 or text[max(0, i-1)].isspace())])
    def get_first_chars_optimized(self, text):
        result = []
        if len(text) <= 1:
            return "" if not text else [text[0]][0]
        first_char_found = False
        i = 0
        while i < len(text):
            char = text[i]
            if char.isspace():
                i += 1
                continue
            first_char_found = True
            while i < len(text):
                current_char = text[i]
                if not current_char.isspace():
                    break
                i += 1
        return "".join(result)
    def get_first_chars_final(self, text):
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        stripped = text.strip()
        if len(stripped) == 0:
            return ""
        result_chars = []
        i = 0
        while i < len(text):
            char = text[i]
            if not char.isspace():
                result_chars.append(char)
                while i < len(text):
                    current_char = text[i]
                    if current_char == ' ':
                        break
                    i += 1
            else:
                i += 1
        return "".join(result_chars)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python Programming is Fun!",
        "   Leading spaces here ",
        "",
        "SingleWord",
        "A B C D E"
    ]
    for case in test_cases:
        output = processor.get_first_chars_final(case)
        print(f'Input: "{case}" -> Output: "{output}"')