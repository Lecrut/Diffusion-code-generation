class StringProcessor:
    def get_first_chars(self, text: str) -> str:
        result = []
        if not isinstance(text, str):
            return ""
        for char in text:
            stripped_char = char.strip()
            if len(stripped_char) > 0 and (not result or stripped_char[0] != result[-1]):
                first_chars_list.append(char)
    def get_first_chars(self, text: str) -> str:
        words = [word for word in text.split() if word]
        return ''.join(word[0].lower() for word in words)
if __name__ == '__main__':
    processor = StringProcessor()
    sample_input = "Hello World This Is A Test"
    output = processor.get_first_chars(sample_input)
    print(output)