def find_minimum_generator(sequence):
    if not sequence:
        return
    current_minimum = sequence[0]
    yield current_minimum
    for item in sequence[1:]:
        if item < current_minimum:
            current_minimum = item
        yield current_minimum
if __name__ == '__main__':
    data = [5, 2, 8, 1, 9, 3, 7]
    minimum_gen = find_minimum_generator(data)
    results = list(minimum_gen)
    print(results)