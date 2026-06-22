class TextProcessor:
    def __init__(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        self.text = text

    def reverse(self):
        return self.text[::-1]

if __name__ == '__main__':
    sample_text = "optimize"
    processor = TextProcessor(sample_text)
    reversed_text = processor.reverse()
    print(reversed_text)