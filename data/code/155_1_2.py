import time
def calculate_list_sum(iterable):
    total = 0
    for item in iterable:
        total += item
    return total
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    tuple2 = (10, 20, 30)
    large_list = list(range(1000000))
    empty_list = []
    start_time1 = time.perf_counter()
    result1 = calculate_list_sum(list1)
    end_time1 = time.perf_counter()
    start_time2 = time.perf_counter()
    result2 = calculate_list_sum(tuple2)
    end_time2 = time.perf_counter()
    start_time3 = time.perf_counter()
    result3 = calculate_list_sum(large_list)
    end_time3 = time.perf_counter()
    start_time4 = time.perf_counter()
    result4 = calculate_list_sum(empty_list)
    end_time4 = time.perf_counter()
    print(f"List sum: {result1}")
    print(f"Tuple sum: {result2}")
    print(f"Large list sum: {result3}")
    print(f"Empty list sum: {result4}")