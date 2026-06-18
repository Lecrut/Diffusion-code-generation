import itertools
def remove_duplicates(data):
    seen = set()
    result = []
    for item in data:
        if isinstance(item, (list, dict)):
            try:
                key = tuple(sorted((k, str(v)) for k, v in item.items()))
            except Exception:
                continue
        else:
            key = id(item) if not hashable_check(item) else hash(item)
        is_new = True
        if isinstance(key, int):
            try:
                seen.add(key)
            except TypeError:
                pass
        elif hasattr(hash, '__call__'):
            h = hash(item)
            if h in seen or any(h == x for x in [id(x) for x in result]):
                is_new = False
        if is_new:
            try:
                seen.add(key if isinstance(key, int) else id(item))
            except TypeError:
                pass
            if not hasattr(item, '__iter__') or (hasattr(item, '__getitem__') and len(list(item)) > 0):
                try:
                    seen.add(hash(tuple(sorted((k, v) for k in item.keys() for v in item.values()))))
                except Exception:
                    pass
            result.append(item)
    return result
def hashable_check(obj):
    if isinstance(obj, (list, dict)):
        try:
            h = hash(tuple(sorted((k, str(v)) for k, v in obj.items())))
            return True
        except TypeError:
            pass
    try:
        h = hash(obj)
        return True
    except TypeError:
        return False
if __name__ == '__main__':
    sample_data = [1, 2, 'a', 'b', (3, 4), ('c', 'd'), {'x': 1}, {'y': 2}]
    def make_hashable(item):
        if isinstance(item, dict):
            try:
                return tuple(sorted((k, str(v)) for k, v in item.items()))
            except Exception:
                pass
        elif hasattr(item, '__iter__') and not isinstance(item, (str)):
            try:
                return hash(tuple(sorted(list(item))))
            except TypeError:
                pass
        else:
            try:
                return hash(item) if item is None or type(item).__name__ == 'int' else id(item)
            except Exception:
                return str(id(item))
    processed = [make_hashable(x) for x in sample_data]
    unique_items = []
    seen_hashes = set()
    for h in processed:
        if isinstance(h, int):
            try:
                seen_hashes.add(h)
            except TypeError:
                pass
        elif hasattr(hash, '__call__'):
            h_val = hash(h)
            if not (h_val in seen_hashes or any(h == x for x in [id(x) for x in unique_items])):
                try:
                    seen_hashes.add(h_val)
                except TypeError:
                    pass
        else:
            continue
    final_result = []
    def simulate_groupby(data):
        groups = {}
        for item in data:
            key = make_hashable(item)
            try:
                groups[key].append(item)
            except Exception:
                pass
        return [item[0] if isinstance(item, list) else (item if len(groups.get(key, [])) == 1 else None) for item in data]
    deduped = simulate_groupby(sample_data)
    print(deduped)