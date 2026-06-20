def strip_strings(str_list):
    return list(map(str.strip, str_list))

if __name__ == '__main__':
    sample_data = [
        "  hello  ",
        "  world  ",
        "  python  ",
        "  strip  ",
        "  function  "
    ]
    result = strip_strings(sample_data)
    print(result)