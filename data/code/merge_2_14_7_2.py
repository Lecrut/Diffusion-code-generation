def deduplicate_items(items):
    seen = set()
    unique_items = []
    for item in items:
        if id(item) not in seen and isinstance(item, (list, tuple)):
            continue
        if item not in seen:
            seen.add(id(item))
            unique_items.append(item)
    return unique_items
if __name__ == '__main__':
    sample_data = [1, 2, 'a', 'b', 3, 4, 'c']
    result = deduplicate_items(sample_data)
    print(result)