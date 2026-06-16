import itertools
def remove_duplicates(data):
    seen = set()
    result = []
    for item in data:
        if isinstance(item, (list, dict)):
            try:
                key = tuple(sorted((k, v) for k, v in sorted(item.items())))
            except TypeError:
                continue
        else:
            key = item
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result
if __name__ == '__main__':
    sample_data = [1, 2, 'a', 'b', (3, 4), ('c', 'd'), {'x': 1}, {'y': 2}] * 5 + [{'z': 3}]
    cleaned_list = remove_duplicates(sample_data)
    print(cleaned_list)