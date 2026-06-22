def calculate_cube_volume(edge_length):
    if not isinstance(edge_length, (int, float)):
        raise TypeError("Edge length must be a number")
    if edge_length <= 0:
        raise ValueError("Edge length must be positive")
    return edge_length * edge_length * edge_length

if __name__ == '__main__':
    edge_value = 3.5
    result = calculate_cube_volume(edge_value)
    print(result)