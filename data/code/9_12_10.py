def trim_spaces(s: str) -> str:
    return s.strip()

if __name__ == '__main__':
    sample_strings = [
        '  hello world  ',
        '   no leading spaces',
        'trailing spaces   ',
        '   both   ',
        'no spaces',
        '   ',
        ''
    ]

    for sample in sample_strings:
        trimmed = trim_spaces(sample)
        print(repr(trimmed))