import time
def count_unique_items(data_list):
    unique_set = set(data_list)
    count = len(unique_set)
    return unique_set, count
if __name__ == '__main__':
    unsorted_list = [1, 2, 3, 4, 1, 5, 2, 6, 3, 7]
    print(f"Original list: {unsorted_list}")
    start_time = time.perf_counter()
    unique_set, unique_count = count_unique_items(unsorted_list)
    end_time = time.perf_counter()
    print(f"Set of unique items: {unique_set}")
    print(f"Number of unique items: {unique_count}")
    print(f"Time taken: {(end_time - start_time) * 1000:.4f} ms")