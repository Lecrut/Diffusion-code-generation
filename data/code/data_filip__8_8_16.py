def split_and_clean(text):
    result = []
    for item in text.split(','):
        cleaned = item.strip()
        if cleaned:
            result.append(cleaned)
    return result

if __name__ == '__main__':
    sample_input = "  apple , banana, , orange , , grape  "
    output = split_and_clean(sample_input)
    print(output)