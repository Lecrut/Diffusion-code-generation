class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word = ''
        for char in text:
            if char.isspace():
                if current_word:
                    words.append(current_word)
                    current_word = ''
            else:
                current_word += char
        if current_word:
            words.append(current_word)
        return ''.join(word[0] for word in words)
if __name__ == '__main__':
    processor = StringProcessor()
    test_input = "Hello World Python Programming"
    result = processor.get_first_chars(test_input)
    print(result)