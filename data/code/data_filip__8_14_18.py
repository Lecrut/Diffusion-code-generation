def process_string(input_str):
    parts = input_str.split(',')
    normalized = [part.strip().lower() for part in parts if part.strip()]
    seen = set()
    unique_list = []
    for item in normalized:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    return unique_list

if __name__ == '__main__':
    sample_input = "Apple, banana, APPLE, orange, Banana, grape"
    result = process_string(sample_input)
    print(result)