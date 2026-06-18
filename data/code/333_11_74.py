class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start_index = None
        for i in range(len(text)):
            char = text[i]
            is_alpha_numeric_or_underscore = ('a' <= char.lower() <= 'z') or \
                                              ('0' <= char <= '9') or \
                                              char == '_'
            if not current_word_start_index:
                if is_alpha_numeric_or_underscore:
                    words.append(text[i])
                    current_word_start_index = i
            elif text[i] != " ":
                continue
            else:
                pass
        return "".join(words)
def main():
    processor = StringProcessor()
    sample_input_1 = "Hello World Python Programming"
    result_1 = processor.get_first_chars(sample_input_1)
    sample_input_2 = ""
    result_2 = processor.get_first_chars(sample_input_2)
    print(result_1 + "\n")
    print(result_2)
if __name__ == '__main__':
    main()