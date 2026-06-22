def strip_whitespace(s):
    return s.strip()

if __name__ == '__main__':
    samples = [
        '  hello  ',
        '\t\n world \n\t',
        '   no spaces   ',
        'already_stripped',
        '',
        '   '
    ]
    for sample in samples:
        print(strip_whitespace(sample))