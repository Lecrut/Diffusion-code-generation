def split_and_trim(s):
    parts = s.split(',')
    result = []
    for part in parts:
        trimmed = part.strip()
        if trimmed:
            result.append(trimmed)
    return result

if __name__ == '__main__':
    sample_string = "  apple , banana , , cherry ,  date "
    result = split_and_trim(sample_string)
    print(result)