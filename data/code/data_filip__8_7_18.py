def split_and_filter(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    parts = text.split(',')
    result = []
    for part in parts:
        stripped = part.strip()
        if stripped:
            result.append(stripped)
    return result

if __name__ == '__main__':
    sample_input = "  apple , banana , , orange , , ,grape "
    output = split_and_filter(sample_input)
    print(output)