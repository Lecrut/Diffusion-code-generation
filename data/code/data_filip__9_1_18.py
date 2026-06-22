def clean_strings(strings_list):
    return [s.strip() for s in strings_list]

if __name__ == '__main__':
    data = ["  hello  ", "  world  ", "  python  "]
    result = clean_strings(data)
    print(result)