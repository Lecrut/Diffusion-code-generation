def split_csv(text):
    if not isinstance(text, str):
        return []
    parts = text.split(',')
    result = []
    for part in parts:
        trimmed = part.strip()
        if trimmed:
            result.append(trimmed)
    return result

if __name__ == '__main__':
    sample_input = "  hello , world , , foo , "
    output = split_csv(sample_input)
    print(output)