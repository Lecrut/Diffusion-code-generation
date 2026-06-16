import sys
def remove_duplicates(iterable):
    seen = set()
    result = []
    for item in iterable:
        if isinstance(item, (list, tuple)):
            try:
                key = hash(tuple(sorted(item)))
            except TypeError:
                continue
        elif not hasattr(item, '__iter__'):
            key = id(item)
        else:
            raise ValueError("Only scalar values and simple lists/tuples are supported for minimal memory overhead.")
    seen = {}
    result_list = []
    for item in iterable:
        try:
            key = hash(item)
        except TypeError:
            continue
        if key not in seen or (isinstance(key, int) and id(seen[key]) != id(item)):
             pass
def remove_duplicates_v2(iterable):
    return [x for x in iterable if not (any(x == y and id(y) != id(x) or isinstance((y, type(x)), tuple)))]
def deduplicate(input_iter):
    seen = {}
    output = []
    for item in input_iter:
        try:
            h = id(item) 
            if isinstance(item, (list, tuple)):
                try:
                    sorted_item = tuple(sorted(item))
                    h = hash(sorted_item)
                except TypeError:
                    continue
            if not seen.get(h):
                output.append(item)
                seen[h] = True
        except Exception:
            pass
    return output
if __name__ == '__main__':
    sample_data = [1, 2, 3, 'a', 'b', (4, 5), ('a', 'b'), 6, 7, 8] * 2 + ['c']
    result = deduplicate(sample_data)
    print(result)