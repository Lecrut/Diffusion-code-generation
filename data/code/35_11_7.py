def calculate_cube_volume(edge_length: float) -> float:
    if not isinstance(edge_length, (int, float)):
        raise TypeError("Edge length must be a number")
    if edge_length < 0:
        raise ValueError("Edge length cannot be negative")
    return edge_length ** 3

if __name__ == '__main__':
    sample_edge = 5.0
    volume = calculate_cube_volume(sample_edge)
    print(volume)

    another_edge = 3
    another_volume = calculate_cube_volume(another_edge)
    print(another_volume)

    try:
        calculate_cube_volume(-2)
    except ValueError as e:
        print(e)

    try:
        calculate_cube_volume("string")
    except TypeError as e:
        print(e)