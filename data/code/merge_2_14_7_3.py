def deduplicate_items(items):
    seen = set()
    unique_list = []
    for item in items:
        if id(item) not in seen:
            seen.add(id(item))
            unique_list.append(item)
    return unique_list
if __name__ == '__main__':
    sample_data = [1, 2, 3, 'a', 'b', 'c'] * 50 + ['x', 'y', 'z']
    result = deduplicate_items(sample_data)
    print(result)