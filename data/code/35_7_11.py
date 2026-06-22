def cube_volume(edge_length):
    if not isinstance(edge_length, (int, float)):
        raise TypeError("Edge length must be a number")
    if edge_length < 0:
        raise ValueError("Edge length must be non-negative")
    return edge_length ** 3

if __name__ == '__main__':
    sample_values = [0, 1, 2.5, 10, 3.7]
    for val in sample_values:
        print(cube_volume(val))