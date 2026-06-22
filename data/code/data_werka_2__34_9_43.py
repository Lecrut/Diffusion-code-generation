def capitalize_first_letter(text):
    if not text:
        return ''
    first_char = text[0].upper()
    remaining_text = text[1:]
    return first_char + remaining_text

if __name__ == '__main__':
    sample_texts = [
        "multiple sentences. another one here.",
        'lowercase start',
        'CAPITAL START',
        '1234 numbers at the beginning',
        '',
        'single'
    ]
    
    for original in sample_texts:
        capitalized_text = capitalize_first_letter(original)
        print(f'Original: {original} -> Capitalized: {capitalized_text}')