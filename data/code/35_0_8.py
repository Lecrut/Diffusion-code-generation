def compute_cube_volume(edge_length):
    return edge_length ** 3

if __name__ == '__main__':
    sample_values = [2, 5.5, 0, -3]
    for val in sample_values:
        print(compute_cube_volume(val))