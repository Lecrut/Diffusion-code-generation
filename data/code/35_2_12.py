def compute_cube_volume(edge_length: float) -> float:
    return edge_length ** 3

if __name__ == '__main__':
    sample_edges = [1, 2.5, 10]
    for edge in sample_edges:
        volume = compute_cube_volume(edge)
        print(volume)