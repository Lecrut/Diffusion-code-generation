def process_items(items):
    filtered = [item for item in items if isinstance(item, (int, float)) and item > 0]
    return sorted(filtered)
if __name__ == '__main__':
    data = [-5, "apple", 3.14, None, -2, 7, "", 99]
    result = process_items(data)
    print(result)