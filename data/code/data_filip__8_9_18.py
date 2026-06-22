def split_and_trim(s):
    if not isinstance(s, str):
        return []
    parts = s.split(',')
    trimmed = [part.strip() for part in parts]
    return [part for part in trimmed if part]

if __name__ == '__main__':
    sample = "  hello , world , , foo , bar  "
    print(split_and_trim(sample))