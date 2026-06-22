def find_zero_difference_index(list_a: list[float], list_b: list[float]) -> int:
    if len(list_a) != len(list_b):
        raise ValueError('Input lists must have the same length')
    for index, (a, b) in enumerate(zip(list_a, list_b)):
        if abs(a - b) < 1e-09:
            return index
    return -1
if __name__ == '__main__':
    list_a = [1.0, 2.5, 3.14, 4.0]
    list_b = [0.5, 2.5, 3.14159, 3.9]
    result = find_zero_difference_index(list_a, list_b)
    print(result)