import heapq
def find_median_iterator(iterable):
    data = []
    for item in iterable:
        data.append(item)
    data.sort()
    n = len(data)
    if n == 0:
        return None
    if n % 2 == 1:
        return data[n // 2]
    else:
        mid1 = data[n // 2 - 1]
        mid2 = data[n // 2]
        return (mid1 + mid2) / 2
if __name__ == '__main__':
    import itertools
    data_generator = (x for x in range(10))
    result1 = find_median_iterator(data_generator)
    print(f"Median of range(10): {result1}")
    data_list = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    result2 = find_median_iterator(iter(data_list))
    print(f"Median of list: {result2}")
    empty_generator = (x for x in [])
    result3 = find_median_iterator(empty_generator)
    print(f"Median of empty: {result3}")
    large_generator = (x for x in range(1000000))
    result4 = find_median_iterator(large_generator)
    print(f"Median of large range: {result4}")