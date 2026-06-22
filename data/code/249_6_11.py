def find_largest_item(items, key):
    if not items:
        return None
    largest = max(items, key=lambda item: item[key])
    return largest

if __name__ == '__main__':
    sample_items = [
        {'name': 'grape', 'weight': 0.5},
        {'name': 'orange', 'weight': 1.0},
        {'name': 'mango', 'weight': 1.5}
    ]
    largest_item = find_largest_item(sample_items, 'weight')
    print(largest_item)