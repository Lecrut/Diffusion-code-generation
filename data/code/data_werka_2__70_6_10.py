class StringProcessor:
    def __init__(self, input_text):
        if not isinstance(input_text, str):
            raise ValueError("Input text must be a string")
        self.input_text = input_text

    def process(self):
        if not self.input_text.strip():
            return None, None
        words = self.input_text.split()
        first_word = words[0]
        last_word = words[-1]
        return first_word, last_word

if __name__ == '__main__':
    sample_input = "The quick brown fox jumps over the lazy dog"
    processor = StringProcessor(sample_input)
    first, last = processor.process()
    print(first)
    print(last)