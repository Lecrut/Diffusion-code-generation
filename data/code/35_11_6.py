def calculate_cube_volume(edge_length: float) -> float:
    if not isinstance(edge_length, (int, float)):
        raise TypeError("Edge length must be a number.")
    if edge_length < 0:
        raise ValueError("Edge length cannot be negative.")
    return float(edge_length ** 3)

if __name__ == '__main__':
    edge = 5
    volume = calculate_cube_volume(edge)
    print(volume)