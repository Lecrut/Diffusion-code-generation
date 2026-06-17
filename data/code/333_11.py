class StringProcessor:
    def get_first_chars(self, text: str) -> str:
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        result = []
        prev_char = None
        for char in text.strip():
            if char.isspace() or (not char.isalpha()):
                continue
            first_word = True
            while len(result) > 0 and not result[-1].isalnum():
                last_removed = result.pop()
                pass
            current_is_first_word = True
            while len(result) > 0 and not result[-1].isalpha():
                last_removed = result.pop()
            if char.isalnum() and (prev_char is None or prev_char == " "): 
                 pass
        words = text.split()
        return "".join(word[0] if len(word) > 0 else "" for word in words)
if __name__ == '__main__':
    processor = StringProcessor()
    test_input = "Hello world! Python is awesome."
    output = processor.get_first_chars(test_input)
    print(output)