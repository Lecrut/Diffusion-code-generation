def cube_volume(edge_length):
    return edge_length ** 3

if __name__ == '__main__':
    sample_edge = 5
    volume = cube_volume(sample_edge)
    print(volume)
    sample_edge = 10
    volume = cube_volume(sample_edge)
    print(volume)