def split_csv(s):
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
    sample_string = "  hello , world ,  python , ,  ,code ,  "
    print(split_csv(sample_string))