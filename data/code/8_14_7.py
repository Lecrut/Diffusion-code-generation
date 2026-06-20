def process_string_input(data):
    if not data:
        return []
    items = data.split(',')
    normalized_items = [item.strip().lower() for item in items if item.strip()]
    seen = set()
    result = []
    for item in normalized_items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    sample_data = " Apple, banana, apple, Orange , BANANA, grape "
    final_list = process_string_input(sample_data)
    print(final_list)