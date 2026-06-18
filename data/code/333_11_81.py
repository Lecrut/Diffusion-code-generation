class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start_index = None
        for i in range(len(text)):
            char = text[i]
            if not any(c.isalpha() or c.isdigit() for c in [char]):
                continue
            prev_char_index = None
            current_word_start_index = i
        return "".join(text[i] for i, char in enumerate(text) 
                      if (i == 0 and text[0].isalnum()) or not any(c.isalpha() or c.isdigit() for c in [text[j]] for j in range(max(0, i-1), min(len(text)+1, i+2)))
                     )
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        result = []
        prev_is_space_or_start = True
        for char in text:
            is_alpha_num = any(c.isalnum() for c in [char])
            if not is_alpha_num:
                prev_is_space_or_start = False
            elif (prev_is_space_or_start) or (not any(c.isalnum() for c in [text[j]] for j in range(max(0, i-1), min(len(text)+1, i+2)))):
                result.append(char)
            prev_is_space_or_start = is_alpha_num
        return "".join(result)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python 3.10 Programming",
        "   Leading spaces ",
        "",
        "SingleWord",
        "A B C D E"
    ]
    for case in test_cases:
        try:
            output = processor.get_first_chars(case)
            print(f'Input: "{case}" -> Output: "{output}"')
        except Exception as e:
            pass
exit(0)