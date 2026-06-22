def cube_volume(edge_length):
    if edge_length < 0:
        return 0.0
    return edge_length ** 3

if __name__ == '__main__':
    print(cube_volume(3.0))