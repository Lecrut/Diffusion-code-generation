EDGE_EXPONENT = 3
SAMPLE_EDGE_LENGTH = 6

def calculate_cube_volume(edge_length):
    return edge_length ** EDGE_EXPONENT

if __name__ == '__main__':
    volume = calculate_cube_volume(SAMPLE_EDGE_LENGTH)
    print(volume)