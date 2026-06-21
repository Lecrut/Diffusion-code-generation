def count_items(lst):
    from collections import defaultdict
    result = defaultdict(int)
    for item in lst:
        try:
            hash(item)
        except TypeError:
            item = tuple(item)
        result[item] += 1
    return dict(result)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 2, (4, 5), (4, 5), [6], [6]]
    print(count_items(sample_list))