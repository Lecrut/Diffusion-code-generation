def split_and_filter(text: str) -> list:
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
    sample_input = "apple, , banana, ,cherry, , , date"
    output = split_and_filter(sample_input)
    print(output)