def calculate_cube_volume(edge_length):
    return edge_length ** 3

if __name__ == '__main__':
    test_edge = 5
    volume = calculate_cube_volume(test_edge)
    print(volume)
    test_edge_large = 10
    volume_large = calculate_cube_volume(test_edge_large)
    print(volume_large)