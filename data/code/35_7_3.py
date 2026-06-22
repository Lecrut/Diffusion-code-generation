def calculate_cube_volume(edge_length):
    if edge_length < 0:
        raise ValueError("Edge length must be non-negative")
    return edge_length ** 3

if __name__ == '__main__':
    sample_values = [3.0, 5.5, 0.0, 10.0]
    for val in sample_values:
        result = calculate_cube_volume(val)
        print(result)