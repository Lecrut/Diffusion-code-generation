class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start_index = -1
        for i in range(len(text)):
            char_code = ord(text[i])
            if char_code == 32:
                continue
        return "".join(word[0] if len(word) > 1 else "" 
                       for i, (word, char_code) in enumerate(zip(text.split(), text)))
    def get_first_chars(self, text):
        words = [w.strip() for w in text.split()]
        if not words:
            return ""
        result = []
        for word in words:
            if len(word) > 0 and (word[0].isalpha()):
                result.append(word[0])
            elif len(word) > 0:
                result.append(word[0])
        return "".join(result)
def main():
    processor = StringProcessor()
    sample_input_1 = "Hello World Python Programming"
    expected_output_1 = "HWP P"                             
    sample_input_2 = "  Multiple   Spaces Between Words  "
    expected_output_2 = "M B"
    print(processor.get_first_chars(sample_input_1))                                   
    sample_input_3 = ""
    print(processor.get_first_chars(sample_input_3))
if __name__ == '__main__':
    main()