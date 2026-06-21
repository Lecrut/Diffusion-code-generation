def capitalize_first_letter(text):
    if not text:
        return ''
    first_char = text[0].upper()
    remaining_text = text[1:]
    return first_char + remaining_text

if __name__ == '__main__':
    SAMPLE_TEXTS = [
        "hello world! this is a test.",
        'another example',
        'yet another one',
        '123 numbers',
        '',
        'singlechar'
    ]
    
    for sample in SAMPLE_TEXTS:
        capitalized_text = capitalize_first_letter(sample)
        print(f'Original: {sample} -> Capitalized: {capitalized_text}')