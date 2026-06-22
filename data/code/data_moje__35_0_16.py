def compute_cube_volume(edge_length):
    return edge_length ** 3

if __name__ == '__main__':
    edge = 4.0
    volume = compute_cube_volume(edge)
    print(volume)
    edge_int = 3
    volume_int = compute_cube_volume(edge_int)
    print(volume_int)