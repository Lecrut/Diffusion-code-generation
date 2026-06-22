def split_and_strip(text):
    if not text:
        return []
    parts = text.split(',')
    result = []
    for part in parts:
        stripped = part.strip()
        result.append(stripped)
    return result

if __name__ == '__main__':
    sample_text = " apple , banana ,cherry , "
    output = split_and_strip(sample_text)
    print(output)