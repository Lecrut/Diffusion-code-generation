def get_middle_element(sequence):
    length = len(sequence)
    if length == 0:
        return None
    lower_bound = (length - 1) // 2
    upper_bound = length // 2
    if lower_bound == upper_bound:
        return sequence[lower_bound]
    sum_values = sequence[lower_bound] + sequence[upper_bound]
    return sum_values // 2

if __name__ == '__main__':
    test_data = [99, 12, 45, 67, 23, 88, 101]
    middle_val = get_middle_element(test_data)
    print(middle_val)