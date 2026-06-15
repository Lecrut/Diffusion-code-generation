def min_max_generator(sequence):
    if not sequence:
        return
    current_min = sequence[0]
    current_max = sequence[0]
    yield current_min
    yield current_max
    for x in sequence[1:]:
        if x < current_min:
            current_min = x
        elif x > current_max:
            current_max = x
        yield current_min
        yield current_max
if __name__ == '__main__':
    data = [10, 5, 20, 3, 15, 25]
    generator = min_max_generator(data)
    results = list(generator)
    print(f"Input sequence: {data}")
    print(f"Minimum value: {results[0]}")
    print(f"Maximum value: {results[1]}")
    range_value = results[1] - results[0]
    print(f"Range: {range_value}")
    data_empty = []
    generator_empty = min_max_generator(data_empty)
    results_empty = list(generator_empty)
    print(f"\nInput sequence: {data_empty}")
    print(f"Results for empty sequence: {results_empty}")