def process_string_data(input_string):
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    parts = input_string.split(',')
    normalized = [part.strip().lower() for part in parts if part.strip()]
    seen = set()
    unique_items = []
    for item in normalized:
        if item not in seen:
            seen.add(item)
            unique_items.append(item)
    return unique_items

if __name__ == '__main__':
    sample_data = "Apple, BANANA, orange, apple, banana, Grape"
    result = process_string_data(sample_data)
    print(result)