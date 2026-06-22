def calculate_cube_volume(edge_length):
    return edge_length ** 3

if __name__ == '__main__':
    test_edge_length = 5
    volume = calculate_cube_volume(test_edge_length)
    print(volume)