def flatten_and_sort(data):
    flat = []
    for item in data:
        if isinstance(item, list) and all(isinstance(x, (int, float)) for x in item):
            flat.extend(item)
        elif isinstance(item, dict):
            values = [v for v in item.values() if isinstance(v, (int, float))]
            flat.extend(values)
    return sorted(flat, key=lambda x: -x)
if __name__ == '__main__':
    sample_data = [[3.14], 50, {'a': [27], 'b': 9}, ['8', 6]]
    result = flatten_and_sort(sample_data)
    print(result)