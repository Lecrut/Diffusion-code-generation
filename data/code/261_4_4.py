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
    n = len(data)
    if n % 2 == 1:
        sorted_data = sorted(data)
        median = sorted_data[n // 2]
        return median
    else:
        sorted_data = sorted(data)
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        median = (mid1 + mid2) / 2.0
        return median
if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    sample_generator = (x for x in sample_list)
    sample_iterator = iter(sample_generator)
    print(f"Sample List: {sample_list}")
    median1 = find_median(sample_list)
    print(f"Median of list: {median1}")
    print("\nSample Generator Data:")
    median2 = find_median(sample_iterator)
    print(f"Median from generator (re-iterating): {median2}")
    empty_iterable = []
    median3 = find_median(empty_iterable)
    print(f"\nMedian of empty list: {median3}")
    single_item = [42]
    median4 = find_median(single_item)
    print(f"Median of single item list: {median4}")
    large_generator = (i for i in range(1000))
    print("\nTesting large generator:")
    median5 = find_median(large_generator)
    print(f"Median of range(1000): {median5}")