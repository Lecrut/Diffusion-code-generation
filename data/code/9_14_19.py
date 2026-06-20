def strip_whitespace(s):
    return s.strip()

if __name__ == '__main__':
    samples = [
        '   hello   ',
        '\t\nworld\t\n',
        'no_change',
        '   ',
        '',
        '\r\n\t  foo  \t\r\n',
        'leading',
        'trailing ',
        '  both  '
    ]
    results = [strip_whitespace(s) for s in samples]
    for r in results:
        print(repr(r))