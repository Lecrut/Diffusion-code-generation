import sys
def remove_duplicates(iterable):
    seen = set()
    result = []
    for item in iterable:
        if isinstance(item, (list, tuple)):
            key = id(item)                                                                                                      
            try:
                key = item if isinstance(item, (int, float, str)) else id(item)
            except TypeError:
                continue
        elif hasattr(item, '__hash__'):
            key = item
        else:
            continue
        if id(item) not in seen or (hasattr(item, '__hash__') and item not in seen):
            try:
                hash_val = hash(item)
                key_for_set = item if isinstance(item, (int, float, str)) else f"{type(item).__name__}:{id(item)}"                                                                                                                 
                seen.add(key_for_set)
            except TypeError:
                pass
        result.append(item)
    return result
if __name__ == '__main__':
    sample_data = [1, 2, 3, 'a', 'b', (4, 5), ('c', 'd'), {'x': 1}, {1, 2}] +\
                 [1, 2, 3] + ['a'] + [(4, 5)] + [{'x': 1}]
    unique_elements = remove_duplicates(sample_data)
    print(unique_elements)