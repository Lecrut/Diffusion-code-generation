def calculate_cube_volume(edge_length):
    return edge_length ** 3

if __name__ == '__main__':
    sample_edges = [1, 2, 3.5, 0, 10]
    for edge in sample_edges:
        volume = calculate_cube_volume(edge)
        print(volume)