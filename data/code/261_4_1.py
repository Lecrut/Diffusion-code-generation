import heapq
def find_median_iterator(iterable):
    data = []
    for item in iterable:
        data.append(item)
    data.sort()
    n = len(data)
    if n == 0:
        return None
    elif n % 2 == 1:
        return data[n // 2]
    else:
        mid1 = data[n // 2 - 1]
        mid2 = data[n // 2]
        return (mid1 + mid2) / 2
if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    sample_generator = (x for x in sample_list)
    sample_iterator = iter(sample_generator)
    result1 = find_median_iterator(sample_list)
    print(f"Median of {sample_list}: {result1}")
    sample_list_even = [1, 5, 2, 8]
    result2 = find_median_iterator(sample_list_even)
    print(f"Median of {sample_list_even}: {result2}")
    empty_iterable = []
    result3 = find_median_iterator(empty_iterable)
    print(f"Median of {empty_iterable}: {result3}")
    sample_generator_data = [10, 4, 7, 2, 9]
    result4 = find_median_iterator(sample_generator_data)
    print(f"Median of generator data: {result4}")