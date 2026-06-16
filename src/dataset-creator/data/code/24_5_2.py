def process_items(items):
    filtered = [item for item in items if isinstance(item, (int, float)) and item > 0]
    return sorted(filtered)
if __name__ == '__main__':
    sample_data = [3.5, "apple", -1, 2, None, 4.7, "", 6, True]
    result = process_items(sample_data)
    print(result)