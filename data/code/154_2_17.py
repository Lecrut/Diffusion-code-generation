def count_items(lst):
    counts = {}
    for item in lst:
        try:
            key = tuple(item) if not isinstance(item, (int, float, str)) else item
            counts[key] = counts.get(key, 0) + 1
        except TypeError:
            continue
    return counts

if __name__ == '__main__':
    sample_list = [1, 'a', [2, 3], (4, 5), 'a', [2, 3], {'b': 6}]
    print(count_items(sample_list))