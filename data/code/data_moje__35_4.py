def calculate_cube_volume(edge_length):
    return edge_length ** 3

if __name__ == '__main__':
    sample_edge = 3.0
    volume = calculate_cube_volume(sample_edge)
    print(volume)
    sample_edge = 5.5
    volume = calculate_cube_volume(sample_edge)
    print(volume)