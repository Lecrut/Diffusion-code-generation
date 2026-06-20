def split_and_trim(text):
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
    sample_text = "  apple , banana, , cherry , kiwi  , "
    output = split_and_trim(sample_text)
    print(output)