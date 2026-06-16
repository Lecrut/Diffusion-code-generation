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
    sample_data = [1, 2, 'a', (3, 4), 5, 'b', 6, 7, 8, 9] * 2 + [(3, 4)]
    cleaned_data = remove_duplicates(sample_data)
    print(cleaned_data)