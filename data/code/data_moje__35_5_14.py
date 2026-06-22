def _validate_edge(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Edge length must be a number")
    if value < 0:
        raise ValueError("Edge length cannot be negative")
    return True

def compute_cube_volume(edge):
    _validate_edge(edge)
    return edge * edge * edge

if __name__ == '__main__':
    sample_edge_length = 12
    computed_volume = compute_cube_volume(sample_edge_length)
    print(computed_volume)