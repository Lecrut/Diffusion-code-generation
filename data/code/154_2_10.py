def count_items(lst):
    counts = {}
    for item in lst:
        if isinstance(item, list):
            item = tuple(item)
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

if __name__ == '__main__':
    sample_list = [1, 'a', [2, 3], 'a', (4, 5), [2, 3]]
    print(count_items(sample_list))