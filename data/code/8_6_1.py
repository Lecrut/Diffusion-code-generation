def split_comma_string(s):
    parts = s.split(',')
    return [part.strip() for part in parts if part.strip()]

if __name__ == '__main__':
    sample1 = "  apple , banana ,  , cherry "
    sample2 = ",,,,"
    sample3 = "hello"
    sample4 = ""
    print(split_comma_string(sample1))
    print(split_comma_string(sample2))
    print(split_comma_string(sample3))
    print(split_comma_string(sample4))