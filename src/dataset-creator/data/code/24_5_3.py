def process_items(items):
    filtered = [item for item in items if isinstance(item, (int, float)) and item > 0]
    return sorted(filtered)
if __name__ == '__main__':
    data = [3, "apple", -5, 2.5, None, 10, "banana"]
    result = process_items(data)
    print(result)