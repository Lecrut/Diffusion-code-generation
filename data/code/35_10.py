def compute_cube_volume(edge_length: float) -> float:
    return edge_length ** 3

if __name__ == '__main__':
    edge_lengths = [2, 3.5, 10]
    for length in edge_lengths:
        print(compute_cube_volume(length))