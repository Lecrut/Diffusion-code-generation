def process_string(sample: str) -> list:
    items = sample.split(',')
    normalized = [item.strip().lower() for item in items]
    seen = set()
    unique_items = []
    for item in normalized:
        if item not in seen:
            seen.add(item)
            unique_items.append(item)
    return unique_items

if __name__ == '__main__':
    sample_input = "Apple, banana, Apple, Orange, banana, grape, Orange"
    result = process_string(sample_input)
    print(result)