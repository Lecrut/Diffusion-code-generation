def _validate_sequence(data):
    if not isinstance(data, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    if len(data) == 0:
        raise ValueError("Sequence must not be empty")
    return data

def get_middle_element(sequence):
    validated = _validate_sequence(sequence)
    size = len(validated)
    if size % 2 == 1:
        return validated[size // 2]
    return validated[size // 2 - 1]

if __name__ == '__main__':
    print(get_middle_element([1, 2, 3, 4, 5]))
    print(get_middle_element([10, 20, 30, 40]))
    print(get_middle_element([99]))
    print(get_middle_element([1, 2]))
    print(get_middle_element([5, 10, 15, 20, 25, 30, 35]))
    print(get_middle_element([7, 8, 9, 10, 11, 12]))