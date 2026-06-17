def find_minimum_generator(sequence):
    if not sequence:
        return
    current_min = sequence[0]
    yield current_min
    for element in sequence[1:]:
        if element < current_min:
            current_min = element
        yield current_min
if __name__ == '__main__':
    data = [5, 2, 8, 1, 9, 3]
    minimum_values = find_minimum_generator(data)
    result = list(minimum_values)
    print(result)