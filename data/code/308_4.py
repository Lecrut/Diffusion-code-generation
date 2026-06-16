import time
def iterative_length(data):
    count = 0
    for _ in data:
        count += 1
    return count
if __name__ == '__main__':
    tuple_data = (1, 2, 3, 4, 5)
    list_data = [10, 20, 30, 40, 50]
    large_list = list(range(1000000))
    start_time_tuple = time.perf_counter()
    length_tuple = iterative_length(tuple_data)
    end_time_tuple = time.perf_counter()
    start_time_list = time.perf_counter()
    length_list = iterative_length(list_data)
    end_time_list = time.perf_counter()
    start_time_large = time.perf_counter()
    length_large = iterative_length(large_list)
    end_time_large = time.perf_counter()
    print(f"Tuple length: {length_tuple}")
    print(f"List length: {length_list}")
    print(f"Large list length: {length_large}")