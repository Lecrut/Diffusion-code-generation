def capitalize_first_letter(text):
    if not text:
        return ''
    first_char = text[0].upper()
    remaining_text = text[1:]
    return first_char + remaining_text

class TextProcessor:
    def __init__(self, text):
        self.text = text

    def process(self):
        return capitalize_first_letter(self.text)

if __name__ == '__main__':
    sample_texts = [
        "hello world! this is a test.",
        'another example',
        'yet another one',
        '123 numbers',
        '',
        'singlechar'
    ]
    
    processor = TextProcessor(sample_texts[0])
    capitalized_text = processor.process()
    print(f'Original: {sample_texts[0]} -> Capitalized: {capitalized_text}')
    
    more_samples = {
        'hello world!': 'Hello world!',
        'this is a test.': 'This is a test.',
        '123 numbers': '123 numbers',
        '': '',
        'singlechar': 'Singlechar'
    }
    
    for original, expected in more_samples.items():
        processor.text = original
        result = processor.process()
        print(f'Original: {original} -> Capitalized: {result} (Expected: {expected})')