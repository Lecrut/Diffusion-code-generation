def get_adjacent_pairs(iterable):
    n = len(iterable)
    if n < 2:
        return []
    pairs = []
    for i in range(n - 1):
        pair = (iterable[i], iterable[i+1])
        pairs.append(pair)
    return pairs
if __name__ == '__main__':
    sample1 = [1, 2, 3, 4, 5]
    result1 = get_adjacent_pairs(sample1)
    print(result1)
    sample2 = ['a', 'b', 'c', 'd']
    result2 = get_adjacent_pairs(sample2)
    print(result2)
    sample3 = [10, 20]
    result3 = get_adjacent_pairs(sample3)
    print(result3)
    sample4 = [5]
    result4 = get_adjacent_pairs(sample4)
    print(result4)
    sample5 = []
    result5 = get_adjacent_pairs(sample5)
    print(result5)