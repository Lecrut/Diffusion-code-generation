def remove_whitespace(text):
    return text.strip()

if __name__ == '__main__':
    samples = [
        '   hello world   ',
        '\t\n  spaces  \n\t',
        'no_extra_spaces',
        '  leading_only',
        'trailing_only  ',
        '',
        '   '
    ]
    for sample in samples:
        result = remove_whitespace(sample)
        print(repr(result))