def normalize_text(text):
    if not isinstance(text, str):
        raise TypeError('Input must be a string')
    normalized = text.strip()
    return normalized
if __name__ == '__main__':
    sample_texts = ['  hello world  ', '   python programming   ', 'no_extra_spaces', '   leading_and_trailing   ', '', '   ']
    for sample in sample_texts:
        result = normalize_text(sample)
        print(repr(result))