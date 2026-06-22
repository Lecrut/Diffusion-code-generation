def calculate_cube_volume(edge_length):
    return edge_length ** 3

if __name__ == '__main__':
    edge = 4.0
    result = calculate_cube_volume(edge)
    print(result)
    edge = 2.5
    result = calculate_cube_volume(edge)
    print(result)