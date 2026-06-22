def unique_chars_sorted(phrase):
    if not isinstance(phrase, str):
        raise ValueError("Input must be a string.")
    return ''.join(sorted(set(phrase)))

if __name__ == '__main__':
    sample_phrase = "hello world"
    try:
        result = unique_chars_sorted(sample_phrase)
        print(result)
    except ValueError as e:
        print(e)