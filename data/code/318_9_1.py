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
    data1 = [1, 2, 3, 4, 5]
    result1 = get_adjacent_pairs(data1)
    print(f"Input: {data1}")
    print(f"Result: {result1}")
    data2 = ['a', 'b', 'c', 'd']
    result2 = get_adjacent_pairs(data2)
    print(f"Input: {data2}")
    print(f"Result: {result2}")
    data3 = [10, 20]
    result3 = get_adjacent_pairs(data3)
    print(f"Input: {data3}")
    print(f"Result: {result3}")
    data4 = [5]
    result4 = get_adjacent_pairs(data4)
    print(f"Input: {data4}")
    print(f"Result: {result4}")
    data5 = []
    result5 = get_adjacent_pairs(data5)
    print(f"Input: {data5}")
    print(f"Result: {result5}")