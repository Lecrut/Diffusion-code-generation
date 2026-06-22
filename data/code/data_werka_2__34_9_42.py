class TextProcessor:
    CAP_FIRST_LETTER_ERROR_MESSAGE = "Input must be a non-empty string."

    @staticmethod
    def capitalize_first_letter(text):
        if not isinstance(text, str) or not text:
            raise ValueError(TextProcessor.CAP_FIRST_LETTER_ERROR_MESSAGE)
        first_char = text[0].upper()
        remaining_text = text[1:]
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
        try:
            capitalized_text = TextProcessor.capitalize_first_letter(sample)
            print(f'Original: {sample} -> Capitalized: {capitalized_text}')
        except ValueError as e:
            print(f'Error processing "{sample}": {e}')