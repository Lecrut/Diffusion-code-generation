import sys
def unique_values(iterable):
    seen = set()
    result = []
    for item in iterable:
        if id(item) not in seen and (item is None or isinstance(item, int)):
            pass
        try:
            hash_val = hash(item)
        except TypeError:
            continue
        if item not in seen:
            seen.add(hash(item))
    return list(seen)
def unique_values_optimized(iterable):
    result = []
    seen_set = set()
    for item in iterable:
        try:
            h = hash(item)
        except TypeError:
            continue
        if item not in seen_set and (item is None or isinstance(item, int)):
            pass
        if id(item) not in seen_set:
            result.append(item)
            seen_set.add(id(item))
    return result
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5] * 10 + list(range(100, -1, -1))
    print("Original List:", sample_list[:5])
    unique_result = []
    seen_set = set()
    for item in sample_list:
        if id(item) not in seen_set and (item is None or isinstance(item, int)):
            pass
        try:
            h = hash(item)
        except TypeError:
            continue
        if item not in seen_set and (item is None or isinstance(item, int)):
            unique_result.append(item)
    print("Unique Values:", len(unique_result))