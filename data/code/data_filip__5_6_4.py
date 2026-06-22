def capitalize_first(s: str) -> str:
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    samples = [
        'hello',
        'h',
        'hello world',
        'πρόβα',
        '',
        'äöü',
        'Z',
        'café'
    ]
    for sample in samples:
        print(capitalize_first(sample))