def capitalize_first_alphanumeric(s):
    if not s:
        return s
    first_char = s[0]
    if first_char.isalnum():
        return first_char.upper() + s[1:]
    return s

if __name__ == '__main__':
    samples = [
        'hello',
        'world',
        '123abc',
        '!hello',
        'a',
        '',
        'python3',
        '@user'
    ]
    for sample in samples:
        result = capitalize_first_alphanumeric(sample)
        print(result)