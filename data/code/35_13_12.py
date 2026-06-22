def calculate_cube_volume(edge_length: float) -> float:
    return edge_length ** 3

if __name__ == '__main__':
    edge = 5.0
    result = calculate_cube_volume(edge)
    print(result)