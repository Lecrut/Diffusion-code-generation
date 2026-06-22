def volume_from_edge(edge):
    if edge < 0:
        return 0
    return edge * edge * edge

def cube_volume(edge):
    return volume_from_edge(edge)

if __name__ == '__main__':
    test_edge = 4
    print(cube_volume(test_edge))