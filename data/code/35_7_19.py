def calculate_cube_volume(edge_length):
    return edge_length ** 3

if __name__ == '__main__':
    sample_edge_1 = 3.5
    sample_edge_2 = 2.0
    result_1 = calculate_cube_volume(sample_edge_1)
    result_2 = calculate_cube_volume(sample_edge_2)
    print(result_1)
    print(result_2)