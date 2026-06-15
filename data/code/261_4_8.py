import heapq
def find_median(iterable):
    data = []
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
            data.append(item)
        except StopIteration:
            break
    if not data:
        return None
    data.sort()
    n = len(data)
    if n % 2 == 1:
        return data[n // 2]
    else:
        mid1 = data[n // 2 - 1]
        mid2 = data[n // 2]
        return (mid1 + mid2) / 2.0
if __name__ == '__main__':
    sample_data_list = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    sample_data_generator = (x for x in sample_data_list)
    sample_data_iterator = iter(sample_data_generator)
    print(f"Median of list: {sample_data_list}")
    median1 = find_median(sample_data_list)
    print(f"Median (List): {median1}")
    print("\nMedian of generator:")
    median2 = find_median(sample_data_generator)
    print(f"Median (Generator): {median2}")
    empty_data = []
    print("\nMedian of empty list:")
    median3 = find_median(empty_data)
    print(f"Median (Empty List): {median3}")
    single_data = [42]
    print("\nMedian of single element list:")
    median4 = find_median(single_data)
    print(f"Median (Single Element): {median4}")