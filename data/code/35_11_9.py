def calculate_cube_volume(edge: float) -> float:
    if edge < 0:
        raise ValueError("Edge length must be non-negative")
    if not isinstance(edge, (int, float)):
        raise TypeError("Edge length must be a number")
    return edge ** 3

if __name__ == '__main__':
    edge_length = 5
    volume = calculate_cube_volume(edge_length)
    print(volume)