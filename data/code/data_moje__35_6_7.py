def calculate_cube_volume(edge_length):
    return edge_length ** 3

if __name__ == '__main__':
    sample_edge = 4
    result = calculate_cube_volume(sample_edge)
    print(result)
    sample_edge_2 = 5
    result_2 = calculate_cube_volume(sample_edge_2)
    print(result_2)