class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start = None
        for char in text:
            if char.isspace():
                if current_word_start is not None and self.is_alphanumeric(current_word_start):
                    words.append(current_word_start)
                    current_word_start = None
            else:
                if current_word_start is None or not self.is_alphanumeric(current_word_start):
                    current_word_start = char
        if current_word_start is not None and self.is_alphanumeric(current_word_start):
            words.append(current_word_start)
        return "".join(words)
    def is_alphanumeric(self, char):
        try:
            ord(char) >= 0 and ord(char) <= 127
            return True
        except TypeError:
            return False
if __name__ == '__main__':
    processor = StringProcessor()
    sample_input = "Hello World! This is a test."
    result = processor.get_first_chars(sample_input)
    print(result)