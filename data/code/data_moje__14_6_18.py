def _validate_sequence(data):
    if not isinstance(data, (list, tuple, range)):
        raise TypeError("Input must be a list, tuple, or range")
    if len(data) < 3:
        raise ValueError("Input must contain at least three elements")

def access_third_from_end(sequence):
    _validate_sequence(sequence)
    return sequence[-3]

if __name__ == '__main__':
    test_data = [5, 15, 25, 35, 45, 55]
    output_value = access_third_from_end(test_data)
    print(output_value)