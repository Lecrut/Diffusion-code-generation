def process_strings(input_string):
    if not input_string:
        return []
    items = input_string.split(',')
    normalized = [item.strip().lower() for item in items if item.strip()]
    seen = set()
    result = []
    for item in normalized:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    sample_input = "Apple, Banana, apple, Orange, banana, Grape"
    final_list = process_strings(sample_input)
    print(final_list)