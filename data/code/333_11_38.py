class StringProcessor:
    def get_first_chars(self, text: str) -> str:
        if not text.strip():
            return ""
        words = []
        current_word = None
        for char in text:
            if char.isalpha() or char.isdigit() or ' ' == char or '\t' == char or '\n' == char:
                if current_word is None and (char.isspace()):
                    continue
                elif not char.isspace():
                    if current_word is None:
                        current_word = [char]
                    else:
                        current_word.append(char)
        result = []
        for word in words:
            if word:
                result.append(word[0])
        return ''.join(result)
if __name__ == '__main__':
    processor = StringProcessor()
    test_input = "Hello world Python is awesome 123"
    output = processor.get_first_chars(test_input)
    print(output)