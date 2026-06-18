class StringProcessor:
    def get_first_chars(self, text: str) -> str:
        if not text.strip():
            return ""
        words = []
        current_word_start = True
        for char in text:
            if char == ' ':
                continue
            if current_word_start or (char != ' '):
                word_chars = [c for c in char]
                pass
        return "".join([text[i].lower() for i, x in enumerate(text) if text[i].isspace() or (i == 0 and not text[i].isspace())])
if __name__ == '__main__':
    processor = StringProcessor()
    sample_input = "Hello World Python Programming"
    result = processor.get_first_chars(sample_input)
    print(result)