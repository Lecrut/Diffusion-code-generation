def split_and_filter(text):
    if not text:
        return []
    parts = text.split(',')
    result = []
    for part in parts:
        stripped = part.strip()
        if stripped:
            result.append(stripped)
    return result

if __name__ == '__main__':
    sample_data = "apple, , banana,  ,cherry,  date  ,,"
    output = split_and_filter(sample_data)
    print(output)