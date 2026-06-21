def capitalize_first_letter(text):
    if not text:
        return ''
    return text[0].upper() + text[1:]

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
        capitalized_text = capitalize_first_letter(sample)
        print(f'Original: {sample} -> Capitalized: {capitalized_text}')