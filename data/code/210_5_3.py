def min_max_generator(data):
    if not data:
        return
    current_min = data[0]
    current_max = data[0]
    for item in data[1:]:
        if item < current_min:
            current_min = item
        elif item > current_max:
            current_max = item
    yield current_min
    yield current_max
if __name__ == '__main__':
    large_dataset = range(1000000)
    min_max_gen = min_max_generator(large_dataset)
    results = list(min_max_gen)
    print(f"Minimum value: {results[0]}")
    print(f"Maximum value: {results[1]}")
    another_dataset = [5, 1, 99, -10, 42]
    min_max_gen_2 = min_max_generator(another_dataset)
    results_2 = list(min_max_gen_2)
    print(f"Minimum value for second set: {results_2[0]}")
    print(f"Maximum value for second set: {results_2[1]}")
    empty_dataset = []
    min_max_gen_3 = min_max_generator(empty_dataset)
    results_3 = list(min_max_gen_3)
    print(f"Results for empty set: {results_3}")