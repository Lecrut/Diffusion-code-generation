def compute_cube_volume(edge_length: float) -> float:
    return edge_length ** 3

if __name__ == '__main__':
    edge = 5.0
    result = compute_cube_volume(edge)
    print(result)