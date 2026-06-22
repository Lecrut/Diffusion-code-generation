def calculate_cube_volume(edge_length):
    if not isinstance(edge_length, (int, float)):
        raise TypeError("edge_length must be a number")
    if edge_length < 0:
        raise ValueError("edge_length cannot be negative")
    return float(edge_length) * float(edge_length) * float(edge_length)

if __name__ == '__main__':
    test_edge_1 = 3.0
    test_edge_2 = 5.5
    volume_1 = calculate_cube_volume(test_edge_1)
    volume_2 = calculate_cube_volume(test_edge_2)
    print(volume_1)
    print(volume_2)