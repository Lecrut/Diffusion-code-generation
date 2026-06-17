class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start_index = None
        for i in range(len(text)):
            char = text[i]
            is_space_before = False
            if i > 0 and text[i-1].isspace():
                is_space_before = True
            if char.isalpha() and (is_space_before or current_word_start_index == None):
                words.append(char)
                current_word_start_index = i
        return "".join(words)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python Programming is Fun!",
        "",
        "   Leading spaces ",
        "NoSpacesHere123",
        "One Two Three Four Five"
    ]
    for case in test_cases:
        result = processor.get_first_chars(case)
        print(f'Input: "{case}" -> Output: "{result}"')