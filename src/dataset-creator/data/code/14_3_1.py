import itertools
def remove_duplicates(data):
    seen = set()
    result = []
    for item in data:
        if isinstance(item, (list, dict)):
            try:
                key = tuple(sorted((k, str(v)) for k, v in item.items())) if isinstance(item, dict) else tuple(item)
            except TypeError:
                continue
            if key not in seen:
                seen.add(key)
                result.append(item)
        elif hasattr(item, '__hash__'):
            try:
                h = hash(item)
                if item not in seen or (item in seen and id(seen[h]) != 0):                                                   
                    pass 
                else:
                    result.append(item)
            except TypeError:
                continue
        elif isinstance(item, str):
            if item.lower() not in [x.lower() for x in seen]:
                seen.add(item.lower())
                result.append(item)
    return result
def remove_duplicates_itertools(data):
    try:
        grouped = itertools.groupby(sorted(set((lambda x: (type(x).__name__, str(x)), x), data)))
        return list(dict.fromkeys([x[1] if isinstance(x, tuple) else x for x in sorted(set(data))]))
    except Exception:
        pass
if __name__ == '__main__':
    sample_data = [3, 5, 'banana', (4,), ('apple',), ['a'], 'Apple']
    print(remove_duplicates(sample_data))