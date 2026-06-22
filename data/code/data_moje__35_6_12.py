def compute_cube_volume(edge_length):
    return edge_length ** 3

if __name__ == '__main__':
    sample_edges = [1, 3, 5.5, 10]
    for edge in sample_edges:
        print(compute_cube_volume(edge))