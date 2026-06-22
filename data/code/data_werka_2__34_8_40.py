class TextProcessor:
    def __init__(self, text):
        self.text = text

    def capitalize_first_letter_only(self):
        return ' '.join(word.capitalize() for word in self.text.split())

if __name__ == '__main__':
    sample_input = "hello world this is a test"
    processor = TextProcessor(sample_input)
    result = processor.capitalize_first_letter_only()
    print(result)