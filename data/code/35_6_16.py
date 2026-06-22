def cube_volume(edge_length):
    side = edge_length
    return side * side * side

if __name__ == '__main__':
    edge_length = 7
    result = cube_volume(edge_length)
    print(result)