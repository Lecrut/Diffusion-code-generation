def calculate_cube_volume(edge_length):
    if edge_length < 0:
        raise ValueError("Edge length cannot be negative")
    return edge_length ** 3

if __name__ == '__main__':
    sample_values = [2.0, 3.5, 0.0, 4.75]
    for val in sample_values:
        result = calculate_cube_volume(val)
        print(f"Edge: {val}, Volume: {result}")