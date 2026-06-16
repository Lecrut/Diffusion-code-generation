import itertools
def remove_duplicates(data):
    seen = set()
    result = []
    for item in data:
        if isinstance(item, (list, tuple)):
            try:
                key = hash(tuple(sorted(item)))
            except TypeError:
                continue
        else:
            key = id(item)
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result
if __name__ == '__main__':
    sample_data = [1, 2, 'a', 'b', (3, 4), [5], 6, ('c', 'd'), 'e']