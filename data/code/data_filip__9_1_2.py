def clean_strings(strings):
    return [s.strip() for s in strings]

if __name__ == '__main__':
    raw_list = ["  hello  ", "  world ", "foo"]
    result = clean_strings(raw_list)
    print(result)