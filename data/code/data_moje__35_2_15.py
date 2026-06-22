def compute_cube_volume(edge_length: float) -> float:
    return edge_length ** 3
if __name__ == '__main__':
    sample_edge_lengths = [1.0, 2.0, 3.5, 10.0]
    for edge in sample_edge_lengths:
        volume = compute_cube_volume(edge)
        print(volume)