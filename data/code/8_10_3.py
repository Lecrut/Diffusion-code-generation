def split_by_comma(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    parts = s.split(',')
    trimmed = [part.strip() for part in parts]
    return trimmed

if __name__ == '__main__':
    sample1 = "  apple , banana ,  cherry "
    sample2 = "one,two,,four, "
    sample3 = ""
    sample4 = "   "
    print(split_by_comma(sample1))
    print(split_by_comma(sample2))
    print(split_by_comma(sample3))
    print(split_by_comma(sample4))