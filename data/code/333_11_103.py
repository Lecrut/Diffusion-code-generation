class StringProcessor:
    def get_first_chars(self, text):
        result = []
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        prev_space = True
        for char in text:
            is_alpha_num = bool(char.isalnum())
            if not prev_space and is_alpha_num:
                continue
            result.append(char)
            prev_space = False if is_alpha_num else True
        return "".join(result).strip()
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = ["Hello World", "  Python   Programming ", "", "a b c d e"]
    for case in test_cases:
        print(processor.get_first_chars(case))