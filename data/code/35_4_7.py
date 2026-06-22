def _validate_edge(edge_length):
    if not isinstance(edge_length, (int, float)):
        raise TypeError("Edge length must be a number")
    if edge_length < 0:
        raise ValueError("Edge length cannot be negative")
    return True

def calculate_cube_volume(edge_length):
    _validate_edge(edge_length)
    return edge_length * edge_length * edge_length

if __name__ == '__main__':
    sample_edges = [2.0, 4.5, 10.0]
    for length in sample_edges:
        volume = calculate_cube_volume(length)
        print(volume)