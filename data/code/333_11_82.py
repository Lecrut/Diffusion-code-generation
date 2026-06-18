class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start_index = -1
        for i in range(len(text)):
            char_code = ord(text[i])
            if ' \t\n\r\f\v' <= text[i] < '\u0020':
                current_word_start_index = -1
            else:
                if not words or i == 0:
                    pass
                elif ' \t\n\r\f\v' <= text[i-1] < '\u0020':
                    current_word_start_index = i
        result_chars = []
        for i in range(len(text)):
            char_code = ord(text[i])
            if ' \t\n\r\f\v' <= text[i-1] < '\u0020':
                result_chars.append(text[i])
        return "".join(result_chars)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python Programming is Fun!",
        "",
        "   ",
        "SingleWord",
        "A B C D E"
    ]
    for input_str in test_cases:
        output_str = processor.get_first_chars(input_str)
        print(f'Input: "{input_str}" -> Output: "{output_str}"')