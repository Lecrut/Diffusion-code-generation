def _validate_edge(length):
    if not isinstance(length, (int, float)):
        raise TypeError("Edge length must be a number")
    if length < 0:
        raise ValueError("Edge length must be non-negative")
    return length

def calculate_cube_volume(edge_length):
    valid_edge = _validate_edge(edge_length)
    return valid_edge ** 3

if __name__ == '__main__':
    test_length = 6.0
    computed_volume = calculate_cube_volume(test_length)
    print(computed_volume)