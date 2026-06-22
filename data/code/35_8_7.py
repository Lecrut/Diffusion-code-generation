CUBE_POWER = 3

def calculate_cube_volume(edge_length):
    return edge_length ** CUBE_POWER

if __name__ == '__main__':
    TEST_EDGE_LENGTH = 7
    computed_volume = calculate_cube_volume(TEST_EDGE_LENGTH)
    print(computed_volume)