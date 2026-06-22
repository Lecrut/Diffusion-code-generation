def _validate_sequence(data):
    if not isinstance(data, (list, tuple)):
        raise ValueError("Input must be a sequence")
    if len(data) == 0:
        raise ValueError("Sequence must not be empty")
    return len(data)

def get_middle_element(data):
    length = _validate_sequence(data)
    is_odd = length % 2 != 0
    if is_odd:
        return data[length // 2]
    return data[length // 2 - 1]

if __name__ == '__main__':
    sample_odd = [4, 8, 15, 16, 23, 42]
    sample_even = [1, 3, 5]
    sample_single = [99]
    print(get_middle_element(sample_odd))
    print(get_middle_element(sample_even))
    print(get_middle_element(sample_single))