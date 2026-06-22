class TextProcessor:
    def __init__(self, text):
        self.text = text

    def capitalize_first_letter(self):
        if not self.text:
            return ''
        first_char = self.text[0].upper()
        remaining_text = self.text[1:]
        return first_char + remaining_text

if __name__ == '__main__':
    sample_texts = [
        "hello world! this is a test.",
        'another example',
        'yet another one',
        '123 numbers',
        '',
        'singlechar'
    ]
    for sample in sample_texts:
        processor = TextProcessor(sample)
        capitalized_text = processor.capitalize_first_letter()
        print(f'Original: {sample} -> Capitalized: {capitalized_text}')