class StringProcessor:
    def get_first_chars(self, text: str) -> str:
        if not text.strip():
            return ""
        words = []
        current_word = []
        for char in text.lower():
            if 'a' <= char <= 'z':
                current_word.append(char)
            elif current_word and (char.isspace() or char == '\n'):
                if len(current_word) > 0:
                    words.append(''.join(current_word))
                    current_word = []
        if current_word:
            words.append(''.join(current_word))
        return ''.join(word[0] for word in words)
if __name__ == '__main__':
    processor = StringProcessor()
    sample_input = "Hello World! This is a test string."
    result = processor.get_first_chars(sample_input)
    print(result)