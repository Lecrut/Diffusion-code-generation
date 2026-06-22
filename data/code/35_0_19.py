def compute_cube_volume(edge_length):
    return edge_length ** 3

if __name__ == '__main__':
    sample_values = [3, 5, 10, 0, -2]
    for val in sample_values:
        print(compute_cube_volume(val))