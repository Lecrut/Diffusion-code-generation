def cube_volume(edge_length):
    side = float(edge_length)
    area = side * side
    return area * side

if __name__ == '__main__':
    test_edge = 7
    calculated_volume = cube_volume(test_edge)
    print(calculated_volume)