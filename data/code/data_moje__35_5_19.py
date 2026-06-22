CUBE_DIMENSION = 3

def compute_cube_volume(edge_length):
    return edge_length ** CUBE_DIMENSION

if __name__ == '__main__':
    test_length = 10
    output_volume = compute_cube_volume(test_length)
    print(output_volume)