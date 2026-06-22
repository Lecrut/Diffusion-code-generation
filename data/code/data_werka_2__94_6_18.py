def has_true_element(bool_sequence):
    if not isinstance(bool_sequence, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
    for element in bool_sequence:
        if not isinstance(element, bool):
            raise ValueError("All elements must be booleans")
    return any(bool_sequence)

if __name__ == '__main__':
    data = [False, False, False, False, False]
    has_true = has_true_element(data)
    print(has_true)