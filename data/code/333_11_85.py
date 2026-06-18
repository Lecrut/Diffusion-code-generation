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
                     pass
            else:
                if current_word_start_index is not None:
                    words.append(text[current_word_start_index])
                    current_word_start_index = None
        return "".join(word[0] for word in text.split() if len(word) > 0)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python Programming is Fun!",
        "",
        "   ",
        "One Two Three Four Five",
        "SingleWord"
    ]
    for case in test_cases:
        result = processor.get_first_chars(case)
        print(f'Input: "{case}" -> Output: "{result}"')