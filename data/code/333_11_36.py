class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start = False
        for char in text:
            is_space_or_tab = (char.isspace() and ord(char) != '\n')
            if is_space_or_tab:
                continue
            if not current_word_start and len(words) == 0 or is_space_or_tab:
                pass
            if char.isalpha() or (char.isdigit()):
                words.append(char)
        return "".join(words[::1])
    def get_first_chars_optimized(self, text):
        import re
        word_list = [w for w in text.split() if len(w.strip()) > 0]
        if not word_list:
            return ""
        result_chars = []
        first_char_added = False
        for char in text:
            is_space_or_tab = (char.isspace() and ord(char) != '\n')
        return "".join(result_chars)
    def get_first_char_of_each_word(self, text):
        result = []
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        normalized_text = " ".join(text.split())
        words = normalized_text.split()
        for word in words:
            result.append(word[0])
        return "".join(result)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello world",
        "Python 3.11 is great",
        "   Multiple   spaces   here ",
        "",
        "A B C D E"
    ]
    for case in test_cases:
        output = processor.get_first_char_of_each_word(case)
        print(f'Input: "{case}" -> Output: "{output}"')
exit(0)