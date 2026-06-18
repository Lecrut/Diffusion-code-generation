import sys
def remove_duplicates(iterable):
    seen = set()
    result = []
    for item in iterable:
        if isinstance(item, (list, tuple)):
            key = str(item)
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
    sample_data = [1, 2, 'a', (3,), 4, 'b', 5, 'c', 6] * 2 + [(7,), 8, 9, 10]
    unique_elements = remove_duplicates(sample_data)
    print(unique_elements)