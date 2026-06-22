def capitalize_first_if_alphanumeric(text):
    if not text:
        return text
    if text[0].isalnum():
        return text[0].upper() + text[1:]
    return text

if __name__ == '__main__':
    samples = [
        'hello world',
        '123 abc',
        '!hello',
        'Python',
        '',
        '   spaced',
        'a',
        '_underscore'
    ]
    for sample in samples:
        result = capitalize_first_if_alphanumeric(sample)
        print(f"Input: {sample!r}, Output: {result!r}")