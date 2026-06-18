class StringProcessor:
    def get_first_chars(self, text: str) -> str:
        if not text.strip():
            return ""
        words = []
        current_word_start = None
        for char in text.split(' '):
            cleaned_char = char.strip()
            if cleaned_char and (not current_word_start or cleaned_char[0] != current_word_start):
                words.append(cleaned_char)
        return ''.join([word[0].strip().upper() for word in words])
if __name__ == '__main__':
    processor = StringProcessor()
    test_input = "hello world, this is a sample string."
    result = processor.get_first_chars(test_input)
    print(result)