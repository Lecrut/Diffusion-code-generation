def compute_cube_volume(edge_length):
    return edge_length ** 3

if __name__ == '__main__':
    sample_edge = 4
    result = compute_cube_volume(sample_edge)
    print(result)
    sample_edge_float = 2.5
    result_float = compute_cube_volume(sample_edge_float)
    print(result_float)