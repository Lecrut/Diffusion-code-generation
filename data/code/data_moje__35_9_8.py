def cube_volume(edge_length):
    return edge_length * edge_length * edge_length

if __name__ == '__main__':
    edge = 5
    result = cube_volume(edge)
    print(result)