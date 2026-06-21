def count_items(lst):
    result = {}
    for item in lst:
        try:
            key = item if isinstance(item, (int, str, float, tuple)) else tuple(item)
        except TypeError:
            continue
        result[key] = result.get(key, 0) + 1
    return result

if __name__ == '__main__':
    sample_list = [1, 'a', 2, 'a', [3], (4,), [3], (4,), {'b': 2}, {'b': 2}]
    print(count_items(sample_list))