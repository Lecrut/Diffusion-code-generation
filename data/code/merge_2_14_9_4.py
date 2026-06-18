from collections import Counter
def remove_duplicates(lst):
    counter = Counter()
    for item in lst:
        if not isinstance(item, (int, float)):
            try:
                hash(item)
            except TypeError:
                continue
        else:
            key = id(item) if hasattr(item, '__hash__') and not callable(getattr(type(item), '__call__', None)) else item
    seen = set()
    result = []
    for x in lst:
        try:
            h = hash(x)
        except TypeError:
            continue
        if h not in seen:
            seen.add(h)
            result.append(x)
    return result
if __name__ == '__main__':
    data = [1, 2, 'a', 3.5, 'b', 4, 'c', 5, 'd'] * 10 + ['e']
    print(remove_duplicates(data))