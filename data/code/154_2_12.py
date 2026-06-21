def count_items(lst):
    counts = {}
    for item in lst:
        try:
            hash(item)
            key = item
        except TypeError:
            key = tuple(item) if isinstance(item, list) else item
        counts[key] = counts.get(key, 0) + 1
    return counts

if __name__ == '__main__':
    sample_list = [1, 2, 2, (3, 4), (3, 4), 'a', 'b', 'a']
    print(count_items(sample_list))