EDGE_THRESHOLD = 1e-9

def calculate_cube_volume(edge_length):
    if edge_length < EDGE_THRESHOLD:
        return 0.0
    return edge_length * edge_length * edge_length

def validate_and_compute(edge):
    if not isinstance(edge, (int, float)):
        raise TypeError("Edge length must be a number")
    if edge < 0:
        raise ValueError("Edge length cannot be negative")
    return calculate_cube_volume(edge)

if __name__ == '__main__':
    sample_edge = 6.0
    computed_volume = validate_and_compute(sample_edge)
    print(computed_volume)