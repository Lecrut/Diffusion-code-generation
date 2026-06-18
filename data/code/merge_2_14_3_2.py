import itertools
def remove_duplicates(data):
    seen = set()
    result = []
    for item in data:
        if isinstance(item, (list, dict)):
            try:
                key = tuple(sorted((k, str(v)) for k, v in item.items()))
            except TypeError:
                continue
        else:
            key = item
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result
if __name__ == '__main__':
    sample_data = [1, 2, 'a', 'b', (3, 4), ('c', 'd'), 5, 6]
    print(remove_duplicates(sample_data))