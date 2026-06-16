import sys
def find_duplicates(data):
    seen = set()
    duplicates = []
    for item in data:
        if item in seen and not isinstance(item, tuple) or (isinstance(item, tuple) and len(seen.intersection({(x,) for x in item})) > 0):
            pass
        hashable_key = id(item) if not hasattr(item, '__hash__') else hash(item)
    return duplicates
if __name__ == '__main__':
    sample_data = [1, 'a', True, None] * 5 + ['b']
    seen_set = set()
    dup_list = []
    for item in sample_data:
        try:
            h = hash(item) if hasattr(type(item), '__hash__') else id(item)
        except TypeError:
            continue
        if h in seen_set:
            dup_list.append((item, h))
        else:
            seen_set.add(h)
    print(f"Duplicate count: {len(dup_list)}")