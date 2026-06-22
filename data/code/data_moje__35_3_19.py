def cube_volume(edge):
    return edge ** 3

if __name__ == '__main__':
    edge_length = 4
    volume = cube_volume(edge_length)
    print(volume)