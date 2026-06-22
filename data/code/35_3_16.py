def cube_volume(edge_length):
    side = edge_length
    volume = side * side * side
    return volume

if __name__ == '__main__':
    length = 7
    print(cube_volume(length))