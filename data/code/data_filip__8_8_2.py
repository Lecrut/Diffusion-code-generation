def split_and_clean(s):
    if not s:
        return []
    parts = s.split(',')
    cleaned = []
    for part in parts:
        stripped = part.strip()
        if stripped:
            cleaned.append(stripped)
    return cleaned

if __name__ == '__main__':
    sample_input = "  apple , banana , , orange ,  , grape "
    result = split_and_clean(sample_input)
    print(result)