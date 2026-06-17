class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word = ''
        for char in text:
            if ' ' <= char <= '~':
                if current_word and (char.isalpha() or char.isdigit()):
                    current_word += char
                else:
                    if len(current_word) > 0:
                        words.append(current_word[0])
                        current_word = ''
        if len(current_word) > 0:
            words.append(current_word[0])
        return ''.join(words)
if __name__ == '__main__':
    processor = StringProcessor()
    test_input = "Hello World Python Programming"
    result = processor.get_first_chars(test_input)
    print(result)