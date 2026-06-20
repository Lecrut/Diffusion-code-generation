def split_and_trim_string(s):
    parts = s.split(',')
    trimmed = [part.strip() for part in parts]
    filtered = [item for item in trimmed if item]
    return filtered

if __name__ == '__main__':
    sample1 = " apple , banana , cherry "
    sample2 = "one,two,,four, "
    sample3 = "   ,   ,  "
    sample4 = ""
    print(split_and_trim_string(sample1))
    print(split_and_trim_string(sample2))
    print(split_and_trim_string(sample3))
    print(split_and_trim_string(sample4))