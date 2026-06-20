def clean_strings(string_list):
    return [s.strip() for s in string_list]

if __name__ == '__main__':
    sample_input = ['  hello  ', '  world  ', 'foo', '  bar  ']
    cleaned = clean_strings(sample_input)
    print(cleaned)