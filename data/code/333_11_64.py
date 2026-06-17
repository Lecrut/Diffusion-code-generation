class StringProcessor:
    def get_first_chars(self, text: str) -> str:
        words = [w.strip() for w in text.split()]
        return ''.join(w[0] if w else '' for w in words)
if __name__ == '__main__':
    processor = StringProcessor()
    sample_input = "Hello world Python programming is fun"
    result = processor.get_first_chars(sample_input)
    print(result)