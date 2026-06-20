def trim_whitespace(s: str) -> str:
    return s.strip()

if __name__ == '__main__':
    sample_values = [
        '  hello world  ',
        '\t\nleading and trailing\t\n',
        '   spaces   ',
        'no_spaces',
        '   a',
        'a   ',
        '  a  b  ',
        '',
        '   ',
        '\x00\x20 \x00hello\x00 \x20\x00'
    ]

    for sample in sample_values:
        result = trim_whitespace(sample)
        print(f'{repr(sample)} -> {repr(result)}')