def count_items(lst):
    counts = {}
    for item in lst:
        key = tuple(item) if not isinstance(item, hashable) else item
        counts[key] = counts.get(key, 0) + 1
    return counts

if __name__ == '__main__':
    sample_list = [1, 2, (3, 4), 'a', 'b', (3, 4)]
    print(count_items(sample_list))