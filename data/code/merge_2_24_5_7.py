def process_items(items):
    filtered = [item for item in items if isinstance(item, (int, float))]
    return sorted(filtered)
if __name__ == '__main__':
    sample_data = ["apple", 30, "banana", -5.2, None, 100]
    result = process_items(sample_data)
    print(result)