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
    data = [10, 5, 20, 3, 15]
    generator = min_max_generator(data)
    results = list(generator)
    print(f"Input sequence: {data}")
    print(f"Minimum value: {results[0]}")
    print(f"Maximum value: {results[1]}")
    range_val = results[1] - results[0]
    print(f"Range: {range_val}")
    data2 = [5, 5, 5, 5]
    generator2 = min_max_generator(data2)
    results2 = list(generator2)
    print(f"\nInput sequence: {data2}")
    print(f"Minimum value: {results2[0]}")
    print(f"Maximum value: {results2[1]}")
    range_val2 = results2[1] - results2[0]
    print(f"Range: {range_val2}")
    data3 = []
    generator3 = min_max_generator(data3)
    results3 = list(generator3)
    print(f"\nInput sequence: {data3}")
    print(f"Results for empty sequence: {results3}")