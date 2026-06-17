def find_min_max(data):
    if not data:
        return
    min_val = data[0]
    max_val = data[0]
    for x in data:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
    yield min_val
    yield max_val
if __name__ == '__main__':
    large_list = [10, -5, 42, 3, 99, -100, 50]
    min_max_generator = find_min_max(large_list)
    results = list(min_max_generator)
    print(results)
    another_list = [1.5, 9.8, 3.14, 0.5, 7.2]
    min_max_generator_2 = find_min_max(another_list)
    results_2 = list(min_max_generator_2)
    print(results_2)
    empty_list = []
    min_max_generator_3 = find_min_max(empty_list)
    results_3 = list(min_max_generator_3)
    print(results_3)