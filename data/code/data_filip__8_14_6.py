def process_string(input_string):
    items = input_string.split(',')
    normalized = [item.strip().lower() for item in items if item.strip()]
    seen = set()
    unique_items = []
    for item in normalized:
        if item not in seen:
            seen.add(item)
            unique_items.append(item)
    return unique_items

if __name__ == '__main__':
    sample_input = "Hello, world, HELLO, python, Python, test"
    result = process_string(sample_input)
    print(result)