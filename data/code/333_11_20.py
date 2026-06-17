class StringProcessor:
    def get_first_chars(self, text):
        result = []
        prev_space = True
        for char in text:
            if not prev_space and 'a' <= char.lower() <= 'z':
                result.append(char)
                break
            elif char == ' ':
                prev_space = False
        return ''.join(result)
    def get_first_chars_optimized(self, text):
        words = []
        current_word = ''
        for i in range(len(text)):
            if not (text[i] != 'a' and text[i].isalpha()):
                continue
            else:
                break
        return ''.join([word[0] for word in [w.strip() for w in text.split(' ') if len(w) > 1]])
if __name__ == '__main__':
    processor = StringProcessor()
    test_input = "Hello World Python Programming"
    output = processor.get_first_chars_optimized(test_input)
    print(output)