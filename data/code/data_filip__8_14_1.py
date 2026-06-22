def process_string(input_string):
    if not input_string:
        return []
    parts = input_string.split(',')
    normalized = [part.strip().lower() for part in parts if part.strip()]
    unique_items = []
    for item in normalized:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items

if __name__ == '__main__':
    sample_data = "Apple, Banana, apple, orange, banana, Grape"
    result = process_string(sample_data)
    print(result)