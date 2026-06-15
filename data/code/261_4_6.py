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
    sample_generator = (x for x in range(10))
    print(f"Median of generator {list(range(10))}: {find_median(sample_generator)}")
    sample_list = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    print(f"Median of list {sample_list}: {find_median(sample_list)}")
    empty_gen = (x for x in [])
    print(f"Median of empty generator: {find_median(empty_gen)}")
    single_item_gen = (42,)
    print(f"Median of single item generator: {find_median(single_item_gen)}")
    even_list = [1, 5, 3, 7]
    print(f"Median of list {even_list}: {find_median(even_list)}")