def repeat_characters(text, n):
    if not isinstance(text, str) or not all((char.isalpha() for char in text)):
        raise ValueError('Text must be a string containing only alphabetic characters.')
    if not isinstance(n, int) or n < 0:
        raise ValueError('Number of repeats must be a non-negative integer.')
    repeated_chars = [char * n for char in text]
    return ''.join(repeated_chars)
if __name__ == '__main__':
    sample_text = 'abc'
    number_of_repeats = 3
    result = repeat_characters(sample_text, number_of_repeats)
    print(result)