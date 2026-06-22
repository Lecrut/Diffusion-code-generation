def split_and_trim(string_value):
    if not string_value:
        return []
    parts = string_value.split(',')
    result = []
    for part in parts:
        trimmed = part.strip()
        if trimmed:
            result.append(trimmed)
    return result

if __name__ == '__main__':
    sample = "  apple , banana,, cherry ,  ,date  "
    values = split_and_trim(sample)
    print(values)