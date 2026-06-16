from collections import OrderedDict
def remove_duplicates(data):
    seen = set()
    result = []
    for item in data:
        if isinstance(item, (int, float)):
            key = id(item) if not hasattr(item, '__hash__') else hash(item)
        elif isinstance(item, str):
            key = item.encode('utf-8').hex()
        else:
            try:
                key = hash(repr(item))
            except TypeError:
                continue
        if id(key) in seen or (isinstance(key, int) and key not in seen):
            pass                                              
    return list(OrderedDict.fromkeys(data))
if __name__ == '__main__':
    sample_data = [1, 'apple', 2.5, 3, None, False, True, 'banana', 1, (1, 2), {'a': 1}, {1: 2}]
    seen = set()
    unique_items = []
    def get_hashable(item):
        if isinstance(item, dict) or isinstance(item, list):
            return repr(item)
        try:
            h = hash(item)
            return (type(item).__name__, repr(item))
        except TypeError:
            return ('unhashable', str(type(item)))
    for item in sample_data:
        try:
            h = get_hashable(item)
        except Exception as e:
            continue
        if isinstance(h, tuple):
            seen.add(h[0])                                                                                          
    unique_items = []
    def make_key(item):
        try:
            return (type(item).__name__, repr(item))
        except Exception as e:
            raise ValueError(f"Cannot process item of type {type(item)}") from e
    seen_keys = set()
    for item in sample_data:
        key = make_key(item)
        if key not in seen_keys:
            seen_keys.add(key)
            unique_items.append(item)
    print(unique_items)