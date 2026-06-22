def find_first_zero_difference_index(list_a: list[float], list_b: list[float]) -> int:
    if len(list_a) != len(list_b):
        raise ValueError('Input lists must have the same length')
    for index in range(len(list_a)):
        difference = list_a[index] - list_b[index]
        if abs(difference) < 1e-09:
            return index
    return -1
if __name__ == '__main__':
    sample_list_a = [1.0, 2.5, 3.14159, 4.0]
    sample_list_b = [0.5, 2.5, 3.1416, 4.0]
    index_of_zero_difference = find_first_zero_difference_index(sample_list_a, sample_list_b)
    print(index_of_zero_difference)