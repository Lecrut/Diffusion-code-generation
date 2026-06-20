def normalize_and_deduplicate(raw_data):
    items = raw_data.split(',')
    normalized_items = []
    for item in items:
        cleaned = item.strip().lower()
        if cleaned not in normalized_items:
            normalized_items.append(cleaned)
    return normalized_items

if __name__ == '__main__':
    sample_input = "Apple, banana, Apple, Cherry, banana, date"
    result = normalize_and_deduplicate(sample_input)
    print(result)