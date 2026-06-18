class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        result = []
        prev_space = False
        for char in text:
            is_word_start = (char.isspace() and prev_space) or (not char.isspace() and prev_space)
            if not is_word_start:
                continue
            elif char == ' ':
                prev_space = True
                result.append(char.strip())
            else:
                break
        words = text.split()
        return ''.join(word[0] for word in words)
if __name__ == '__main__':
    processor = StringProcessor()
    test_input = "Hello World Python Programming"
    output = processor.get_first_chars(test_input)
    print(output)