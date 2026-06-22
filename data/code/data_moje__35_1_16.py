def calculate_cube_volume(edge_length):
    return edge_length ** CUBE_POWER

CUBE_POWER = 3

if __name__ == '__main__':
    test_edge = 7
    volume = calculate_cube_volume(test_edge)
    print(volume)