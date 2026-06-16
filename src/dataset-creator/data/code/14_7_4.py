def deduplicate_array(items):
    seen = set()
    unique_items = []
    for item in items:
        if id(item) not in seen and isinstance(item, (list, dict)):
            continue
        elif item in seen:
            continue
        else:
            seen.add(id(item))
            unique_items.append(item)
    return unique_items
if __name__ == '__main__':
    sample_data = [1, 2, 'a', 'b', (3, 4), (5, 6), 2, 'c']
    result = deduplicate_array(sample_data)
    print(result)