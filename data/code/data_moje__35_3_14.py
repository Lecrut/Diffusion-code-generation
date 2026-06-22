def _validate_edge_length(length):
    if length < 0:
        raise ValueError("Edge length cannot be negative")
    if not isinstance(length, (int, float)):
        raise TypeError("Edge length must be a number")
    return length

def calculate_cube_volume(edge_length):
    validated_length = _validate_edge_length(edge_length)
    return validated_length ** 3

if __name__ == '__main__':
    test_edge = 4.5
    volume = calculate_cube_volume(test_edge)
    print(volume)