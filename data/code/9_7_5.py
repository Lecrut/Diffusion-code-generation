def normalize_text(text):
    normalized = text.strip()
    return normalized

if __name__ == '__main__':
    sample_inputs = [
        '  hello world  ',
        '  python  programming  ',
        '   ',
        'no_extra_spaces',
        '  mixed   spaces  '
    ]
    for sample in sample_inputs:
        result = normalize_text(sample)
        print(repr(result))