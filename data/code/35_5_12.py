CUBE_POWER = 3

def validate_edge(edge):
    if not isinstance(edge, (int, float)):
        raise TypeError("Edge length must be a number")
    if edge < 0:
        raise ValueError("Edge length cannot be negative")

def compute_volume(base, exponent):
    return base ** exponent

def cube_volume(edge_length):
    validate_edge(edge_length)
    return compute_volume(edge_length, CUBE_POWER)

if __name__ == '__main__':
    sample_edge_length = 6.2
    calculated_volume = cube_volume(sample_edge_length)
    print(calculated_volume)