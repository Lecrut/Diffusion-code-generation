def process_items(items):
    filtered = [item for item in items if isinstance(item, (int, float))]
    return sorted(filtered)
if __name__ == '__main__':
    data = ["apple", 30, "banana", -5.2, None, True]
    result = process_items(data)
    print(result)