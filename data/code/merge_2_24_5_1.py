def process_items(items):
    filtered = [item for item in items if isinstance(item, (int, float)) and item > 0]
    return sorted(filtered)
if __name__ == '__main__':
    data = [3.5, "apple", -2, 10, None, 4, "banana"]
    result = process_items(data)
    print(result)