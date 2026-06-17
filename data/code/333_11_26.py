class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start_index = None
        for i in range(len(text)):
            char = text[i]
            is_alpha_numeric_or_underscore = ('a' <= char.lower() <= 'z') or \
                                              ('0' <= char.upper() <= '9') or \
                                              char == '_'
            if not current_word_start_index:
                words.append(char)
                current_word_start_index = i
            elif is_alpha_numeric_or_underscore and text[i-1] != " ":
                pass
        return "".join(words).strip()
if __name__ == '__main__':
    processor = StringProcessor()
    sample_input = "Hello World! This is a test string."
    result = processor.get_first_chars(sample_input)
    print(result)