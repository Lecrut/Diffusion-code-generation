import itertools
def remove_duplicates(items):
    if not items:
        return []
    try:
        seen = set()
        result = []
        for item in items:
            key = (item,) if isinstance(item, tuple) else item
            if key not in seen:
                seen.add(key)
                result.append(item)
        return result
    except TypeError:
        grouped = itertools.groupby(items)
        return [key for _, group in grouped]
if __name__ == '__main__':
    sample_data = [[1, 2], [3, 4], [1, 2], 'a', 'b', 'c']
    print(remove_duplicates(sample_data))