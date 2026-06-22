def calculate_cube_volume(edge_length: float) -> float:
    return edge_length ** 3

if __name__ == '__main__':
    result = calculate_cube_volume(5)
    print(result)