def capitalize_first_letter(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    if not text:
        return ''
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
            capitalized_text = capitalize_first_letter(sample)
            print(f'Original: {sample} -> Capitalized: {capitalized_text}')
        except ValueError as e:
            print(f'Error processing "{sample}": {e}')