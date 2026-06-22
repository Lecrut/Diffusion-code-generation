def strip_whitespace(s: str) -> str:
    return s.strip()

if __name__ == '__main__':
    test_cases = [
        '  hello world  ',
        '\t\tPython\t\t',
        '\n\n   spaces   \n\n',
        'no_extra',
        '   multiple   spaces   here   ',
        '',
        '   ',
    ]
    for case in test_cases:
        result = strip_whitespace(case)
        print(repr(result))