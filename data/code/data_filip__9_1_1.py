def clean_strings(string_list):
    return [s.strip() for s in string_list]

if __name__ == '__main__':
    sample_data = ['  hello  ', 'world  ', '  test', '  data  ']
    result = clean_strings(sample_data)
    print(result)