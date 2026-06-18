class StringProcessor:
    def get_first_chars(self, text: str) -> str:
        if not text.strip():
            return ""
        words = []
        current_word = []
        in_word = False
        for char in text.lower():
            if 'a' <= char <= 'z':
                if not in_word and len(current_word) == 0:
                    pass 
                current_word.append(char)
                in_word = True
            elif char.isspace():
                if current_word or 'a' <= char.lower() <= 'z':
                    words.append(''.join(current_word))
                    current_word = []
                    in_word = False
        if current_word:
            words.append(''.join(current_word))
        return ''.join(word[0] for word in words)
if __name__ == '__main__':
    processor = StringProcessor()
    sample_input = "Hello World! Python is awesome."
    result = processor.get_first_chars(sample_input)
    print(result)