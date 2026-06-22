def _is_valid_sequence(data):
    return isinstance(data, list) and len(data) >= 2

def get_pre_last_element(sequence):
    if not _is_valid_sequence(sequence):
        raise ValueError("Sequence must contain at least two elements")
    return sequence[-2]

if __name__ == '__main__':
    test_values = ["alpha", "beta", "gamma", "delta", "epsilon"]
    result = get_pre_last_element(test_values)
    print(result)