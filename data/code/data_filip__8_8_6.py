def split_and_clean(s):
    parts = s.split(',')
    cleaned = []
    for part in parts:
        stripped = part.strip()
        if stripped:
            cleaned.append(stripped)
    return cleaned

if __name__ == '__main__':
    sample = "apple, banana, , cherry,  date ,,"
    result = split_and_clean(sample)
    print(result)