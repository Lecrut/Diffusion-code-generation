def calculate_cube_volume(edge_length):
    return edge_length ** 3

if __name__ == '__main__':
    edge = 5
    volume = calculate_cube_volume(edge)
    print(volume)