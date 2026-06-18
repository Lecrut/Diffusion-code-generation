import sys
def find_duplicates(data):
    seen = set()
    duplicates = []
    for item in data:
        if isinstance(item, (list, tuple)):
            try:
                hashable_item = frozenset(sorted(map(str.lower, map(str.strip, item))))
            except TypeError:
                continue
        elif not hasattr(item, '__hash__'):
            continue
        else:
            if item in seen:
                duplicates.append(item)
            else:
                seen.add(item)
    return set(duplicates)
if __name__ == '__main__':
    sample_data = [1, 2, 'apple', (3, 4), 'banana', ('apple',), 5, 'Apple']
    duplicates = find_duplicates(sample_data)
    print(f"Duplicate values found: {duplicates}")