def split_normalize_unique(input_string):
    parts = input_string.split(',')
    normalized = [part.strip().lower() for part in parts]
    seen = set()
    result = []
    for item in normalized:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    sample_input = "Apple, banana, Apple, CHERRY, banana, date"
    output = split_normalize_unique(sample_input)
    print(output)