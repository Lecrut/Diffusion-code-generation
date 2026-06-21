def filter_unique_items(items):
    seen = set()
    unique_items = []
    for item in items:
        if item not in seen:
            seen.add(item)
            unique_items.append(item)
    return unique_items

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry', 'date', 'apple']
    filtered_items = filter_unique_items(sample_items)
    print(filtered_items)