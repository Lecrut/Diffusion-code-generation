class TextProcessor:
    def __init__(self):
        self.translation_table = str.maketrans('', '', ' ')

    def process_text(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return text.translate(self.translation_table)

if __name__ == '__main__':
    processor = TextProcessor()
    sample_texts = [
        "This is the first sample with spaces.",
        'Here is another example without spaces.',
        "One more variant to test the function."
    ]
    for text in sample_texts:
        print(processor.process_text(text))