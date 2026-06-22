def get_boundary_values(seq):
    if not seq:
        raise ValueError("Sequence must contain at least one element")
    first_index = 0
    last_index = -1
    first_value = seq[first_index]
    last_value = seq[last_index]
    return first_value, last_value

if __name__ == '__main__':
    test_data = [100, 250, 75, 300, 50]
    start, end = get_boundary_values(test_data)
    print(start, end)