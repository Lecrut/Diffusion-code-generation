def capitalize_first_letter(text):
    if not text:
        return ''
    first_char = text[0].upper()
    remaining_text = text[1:]
    return first_char + remaining_text

class TextProcessor:
    def __init__(self, texts):
        self.texts = texts

    def process_texts(self):
        results = {}
        for original in self.texts:
            capitalized = capitalize_first_letter(original)
            results[original] = capitalized
        return results

if __name__ == '__main__':
    sample_texts = [
        "hello world! this is a test.",
        'another example',
        'yet another one',
        '123 numbers',
        '',
        'singlechar'
    ]
    processor = TextProcessor(sample_texts)
    processed_results = processor.process_texts()
    
    for original, capitalized in processed_results.items():
        print(f'Original: {original} -> Capitalized: {capitalized}')