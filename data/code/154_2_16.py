def count_items(lst):
    counts = {}
    for item in lst:
        key = tuple(item) if not isinstance(item, hashable) else item
        counts[key] = counts.get(key, 0) + 1
    return counts

if __name__ == '__main__':
    sample_list = [1, 2, 3, (4, 5), 'a', 'b', 'a', (4, 5)]
    print(count_items(sample_list))