def count_items(lst):
    counts = {}
    for item in lst:
        try:
            key = item if isinstance(item, hashable) else tuple(item)
        except TypeError:
            continue
        counts[key] = counts.get(key, 0) + 1
    return counts

if __name__ == '__main__':
    sample_list = [1, 2, 3, 1, 'a', 'b', 'a', (1, 2), (1, 2), [1, 2], [1, 2]]
    print(count_items(sample_list))