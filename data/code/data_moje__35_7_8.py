def calculate_cube_volume(edge_length):
    if not isinstance(edge_length, (int, float)):
        raise TypeError("Edge length must be a number")
    if edge_length < 0:
        raise ValueError("Edge length must be non-negative")
    return edge_length ** 3

if __name__ == '__main__':
    print(calculate_cube_volume(2.5))
    print(calculate_cube_volume(3))
    print(calculate_cube_volume(0))