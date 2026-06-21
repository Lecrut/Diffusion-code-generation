def capitalize_first_letter(text):
    if not text:
        return ''
    
    first_char = text[0].upper()
    remaining_text = text[1:]
    capitalized_text = first_char + remaining_text
    return capitalized_text

if __name__ == '__main__':
    sample_text = "multiple words in this sentence."
    result = capitalize_first_letter(sample_text)
    print(result)

    more_samples = {
        'another example': 'Another example',
        'yet another one': 'Yet another one',
        '123 numbers': '123 numbers',
        '': '',
        'singlechar': 'Singlechar'
    }
    
    for original, expected in more_samples.items():
        result = capitalize_first_letter(original)
        print(f'Original: {original} -> Capitalized: {result} (Expected: {expected})')