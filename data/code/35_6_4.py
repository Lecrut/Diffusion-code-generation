def compute_cube_volume(edge_length):
    return edge_length ** 3

if __name__ == '__main__':
    sample_edge_lengths = [2, 5, 10.5, 1]
    for edge in sample_edge_lengths:
        volume = compute_cube_volume(edge)
        print(volume)