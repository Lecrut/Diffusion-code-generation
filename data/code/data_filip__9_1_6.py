def clean_strings(strings):
    return [s.strip() for s in strings]

if __name__ == '__main__':
    sample_list = ['  hello  ', 'world   ', '  python ', '  ']
    result = clean_strings(sample_list)
    print(result)