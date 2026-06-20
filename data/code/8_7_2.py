def split_and_filter(text):
    if not text:
        return []
    results = []
    parts = text.split(',')
    for part in parts:
        cleaned = part.strip()
        if cleaned:
            results.append(cleaned)
    return results

if __name__ == '__main__':
    sample_input = "  apple,  banana , , orange,  , grape  "
    output = split_and_filter(sample_input)
    print(output)