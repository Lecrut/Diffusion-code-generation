def split_and_trim(text):
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
    sample_text = "  hello , world ,  , python ,  "
    values = split_and_trim(sample_text)
    print(values)