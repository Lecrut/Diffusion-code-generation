def clean_strings(string_list):
    return [s.strip() for s in string_list]

if __name__ == '__main__':
    sample = ["  hello  ", "  world ", "foo", "  bar  "]
    result = clean_strings(sample)
    print(result)