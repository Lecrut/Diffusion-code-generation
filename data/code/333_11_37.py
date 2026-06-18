class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start = False
        for char in text:
            if 'a' <= char.lower() <= 'z':
                if not current_word_start and (char.isalpha()):
                    words.append(char)
                    current_word_start = True
                elif current_word_start:
                    continue
        return ''.join(words)
if __name__ == '__main__':
    processor = StringProcessor()
    sample_input = "Hello World! Python Programming is Fun."
    result = processor.get_first_chars(sample_input)
    print(result)