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
    sample_data_list = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    sample_data_generator = (x for x in sample_data_list)
    print(f"Median of list {sample_data_list}: {find_median_iterator(sample_data_list)}")
    print(f"Median of generator: {find_median_iterator(sample_data_generator)}")
    empty_data = []
    print(f"Median of empty list: {find_median_iterator(empty_data)}")
    single_data = [42]
    print(f"Median of single element list: {find_median_iterator(single_data)}")
    even_data = [1, 5, 3, 7]
    print(f"Median of even data: {find_median_iterator(even_data)}")