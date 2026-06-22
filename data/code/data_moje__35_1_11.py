def _validate_edge_length(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Edge length must be a number")
    if value <= 0:
        raise ValueError("Edge length must be positive")
    return True

def calculate_cube_volume(edge_length):
    _validate_edge_length(edge_length)
    return edge_length ** 3

if __name__ == '__main__':
    SAMPLE_EDGE = 4.2
    volume = calculate_cube_volume(SAMPLE_EDGE)
    print(volume)