def _validate_sequence(input_data):
    if not hasattr(input_data, '__len__'):
        raise ValueError("Input must have a length")
    if len(input_data) == 0:
        raise ValueError("Input must be non-empty")
    return True

def get_edge_elements(input_data):
    _validate_sequence(input_data)
    return (input_data[0], input_data[-1])

if __name__ == '__main__':
    test_list = [7, 14, 21, 28, 35]
    result = get_edge_elements(test_list)
    print(result)