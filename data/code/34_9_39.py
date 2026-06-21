def capitalize_first_letter(text):
    if not text:
        return ''
    first_char = text[0].upper()
    remaining_text = text[1:]
    return first_char + remaining_text
if __name__ == '__main__':
    sample_text = 'hello world! this is a test.'
    capitalized_text = capitalize_first_letter(sample_text)
    print(capitalized_text)
    more_samples = {'another example': 'Another example', 'yet another one': 'Yet another one', '123 numbers': '123 numbers', '': '', 'singlechar': 'Singlechar'}
    for original, expected in more_samples.items():
        result = capitalize_first_letter(original)
        print(f'Original: {original} -> Capitalized: {result} (Expected: {expected})')