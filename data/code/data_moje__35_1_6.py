def calculate_cube_volume(edge_length):
    _validate_edge(edge_length)
    return _compute_cubed(edge_length)

def _validate_edge(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Edge must be numeric")
    if value < 0:
        raise ValueError("Edge must be non-negative")

def _compute_cubed(edge):
    return edge * edge * edge

if __name__ == '__main__':
    test_edge = 4
    vol = calculate_cube_volume(test_edge)
    print(vol)