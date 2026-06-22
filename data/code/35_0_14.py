def _validate_edge(edge_length):
    if not isinstance(edge_length, (int, float)):
        raise TypeError("Edge length must be a number")
    if edge_length < 0:
        raise ValueError("Edge length must be non-negative")

def compute_cube_volume(edge_length):
    _validate_edge(edge_length)
    return edge_length ** 3

if __name__ == '__main__':
    val1 = 2
    val2 = 7.5
    val3 = 0
    print(compute_cube_volume(val1))
    print(compute_cube_volume(val2))
    print(compute_cube_volume(val3))