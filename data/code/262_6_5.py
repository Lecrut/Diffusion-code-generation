def find_min_max(data):
    if not data:
        return
    minimum = data[0]
    maximum = data[0]
    for number in data:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number
    yield minimum
    yield maximum
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 8]
    min_max_generator = find_min_max(sample_list)
    results = list(min_max_generator)
    print(results)
    large_list = [1000000, -500000, 999999, 0, 500000]
    min_max_generator_large = find_min_max(large_list)
    results_large = list(min_max_generator_large)
    print(results_large)
    empty_list = []
    min_max_generator_empty = find_min_max(empty_list)
    results_empty = list(min_max_generator_empty)
    print(results_empty)