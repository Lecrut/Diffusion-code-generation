def calculate_cube_volume(edge_length):
    return edge_length ** 3

if __name__ == '__main__':
    sample_edges = [2.0, 3.5, 0.0, 10.123]
    for edge in sample_edges:
        print(calculate_cube_volume(edge))