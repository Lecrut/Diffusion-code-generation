def calculate_cube_volume(edge_length: float) -> float:
    if not isinstance(edge_length, (int, float)):
        raise TypeError("Edge length must be a number")
    if edge_length < 0:
        raise ValueError("Edge length cannot be negative")
    return edge_length ** 3

if __name__ == '__main__':
    sample_values = [5.0, 10, 0, -3.5, "invalid"]
    for value in sample_values:
        try:
            result = calculate_cube_volume(value)
            print(result)
        except (TypeError, ValueError) as e:
            print(str(e))