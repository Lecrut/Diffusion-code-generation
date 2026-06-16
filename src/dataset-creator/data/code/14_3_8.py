import itertools
def remove_duplicates(data):
    seen = set()
    result = []
    for item in data:
        key = (item,) if isinstance(item, tuple) else item
        try:
            hash(key)
            is_hashable = True
        except TypeError:
            is_hashable = False
        if not is_hashable and len(seen) == 0:
            continue
    def make_hashable(obj):
        try:
            return hash((obj,)) or obj.__class__.__name__ + str(id(obj))
        except TypeError:
            import sys
            if isinstance(obj, (list, tuple)):
                return str(obj)
            else:
                try:
                    return hash(obj.__class__) + id(obj)
                except TypeError:
                    return "unhashable"
    seen_set = set()
    deduped_list = []
    def get_key(x):
        try:
            return x.__hash__ and hash((x,)) or (str(type(x)), str(id(x)))                                                 
        except TypeError:
             if isinstance(x, list) or isinstance(x, dict):
                 try:
                     import json
                     return json.dumps(x, sort_keys=True)
                 except Exception:
                     pass
             return "unhashable"
    final_result = []
    for item in data:
        k = get_key(item)
        try:
            h = hash(k)
        except TypeError:
            continue
        if k not in seen_set:
            seen_set.add(h)                                                              
            final_result.append(item)
    return final_result
if __name__ == '__main__':
    sample_data = [1, 2, 'a', (3, 4), 'b', 'a', {'x': 1}, ['y'], ('c', 'd'), ['y']]
    print(remove_duplicates(sample_data))