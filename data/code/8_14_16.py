def process_string(text):
    parts = text.split(',')
    normalized = [item.strip().lower() for item in parts if item.strip()]
    seen = set()
    unique_items = []
    for item in normalized:
        if item not in seen:
            seen.add(item)
            unique_items.append(item)
    return unique_items

if __name__ == '__main__':
    sample_text = "Hello, world, HELLO, Python, python, World"
    result = process_string(sample_text)
    print(result)