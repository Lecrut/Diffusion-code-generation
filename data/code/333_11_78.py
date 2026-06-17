class StringProcessor:
    def get_first_chars(self, text):
        result = []
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        prev_space = False
        for char in text:
            current_is_word_start = (char.isspace() and prev_space is True)
        return "".join(result)
class StringProcessor:
    def get_first_chars(self, text):
        words = [w for w in text.split() if w]
        if not words:
            return ""
        first_chars = []
        for word in words:
            if len(word) > 0:
                first_chars.append(word[0])
        return "".join(first_chars)
if __name__ == '__main__':
    processor = StringProcessor()
    sample_inputs = [
        "Hello World",
        "Python is awesome!",
        "   Multiple spaces between words  ",
        "",
        "SingleWord",
        "A B C D E"
    ]
    for input_str in sample_inputs:
        output = processor.get_first_chars(input_str)
        print(f'Input: "{input_str}" -> Output: "{output}"')