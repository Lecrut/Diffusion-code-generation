import sys
def remove_duplicates(iterable):
    seen = set()
    result = []
    for item in iterable:
        if isinstance(item, (list, tuple)):
            key = hash(tuple(sorted(item)))
        else:
            try:
                key = id(item)
            except TypeError:
                continue
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result
if __name__ == '__main__':
    data = [1, 2, 'a', (3, 4), 5, (3, 4), 6]
    unique_data = remove_duplicates(data)
    print(unique_data)