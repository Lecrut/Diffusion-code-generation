def capitalize_first_chars(strings):
    return [s[0].upper() + s[1:] if s else s for s in strings]

if __name__ == '__main__':
    sample_strings = ['hello', 'world', '', 'python']
    result = capitalize_first_chars(sample_strings)
    print(result)