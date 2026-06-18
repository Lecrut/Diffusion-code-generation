def deduplicate_array(items):
    seen = set()
    result = []
    for item in items:
        if id(item) not in seen:
            seen.add(id(item))
            result.append(item)
    return result
if __name__ == '__main__':
    sample_data = [1, 2, 3, 'a', 'b', 'c'] * 50 + ['x', 'y', 'z']
    unique_items = deduplicate_array(sample_data)
    print(unique_items)