import timeit
def find_unique_items(item_names):
    result = {}
    for item in item_names:
        result[item] = True
    return result
if __name__ == '__main__':
    sample_names_1 = ["apple", "banana", "apple", "orange", "banana"]
    sample_names_2 = ["cat", "dog", "mouse", "cat", "dog", "bird"]
    sample_names_3 = ["a", "b", "c", "d", "e"]
    start_time_1 = timeit.default_timer()
    result_1 = find_unique_items(sample_names_1)
    end_time_1 = timeit.default_timer()
    start_time_2 = timeit.default_timer()
    result_2 = find_unique_items(sample_names_2)
    end_time_2 = timeit.default_timer()
    start_time_3 = timeit.default_timer()
    result_3 = find_unique_items(sample_names_3)
    end_time_3 = timeit.default_timer()
    print("Result 1:", result_1)
    print("Time taken for Sample 1:", (end_time_1 - start_time_1))
    print("Result 2:", result_2)
    print("Time taken for Sample 2:", (end_time_2 - start_time_2))
    print("Result 3:", result_3)
    print("Time taken for Sample 3:", (end_time_3 - start_time_3))