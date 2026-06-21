def get_second_to_last(sequence):
    length = len(sequence)
    if length < 2:
        raise ValueError("Sequence must contain at least two elements")
    return sequence[-2]

if __name__ == '__main__':
    test_data = [1, 2, 3, 4, 5]
    value = get_second_to_last(test_data)
    print(value)