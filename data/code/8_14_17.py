def normalize_and_deduplicate(input_string):
    items = input_string.split(',')
    normalized = []
    for item in items:
        cleaned = item.strip().lower()
        if cleaned and cleaned not in normalized:
            normalized.append(cleaned)
    return normalized

if __name__ == '__main__':
    sample_data = "Apple, Banana, apple, orange, BANANA, Grape"
    result = normalize_and_deduplicate(sample_data)
    print(result)