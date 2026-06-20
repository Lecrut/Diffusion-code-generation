def split_and_trim(s):
    if not isinstance(s, str):
        return []
    parts = s.split(',')
    result = []
    for part in parts:
        trimmed = part.strip()
        if trimmed:
            result.append(trimmed)
    return result

if __name__ == '__main__':
    sample1 = " apple , banana , cherry , "
    sample2 = "  ,  , orange,   grape  ,  "
    sample3 = ""
    sample4 = "single_item"
    sample5 = ",,,,"
    print(split_and_trim(sample1))
    print(split_and_trim(sample2))
    print(split_and_trim(sample3))
    print(split_and_trim(sample4))
    print(split_and_trim(sample5))