def cube_volume(edge):
    if edge < 0:
        return 0
    return edge * edge * edge

if __name__ == '__main__':
    print(cube_volume(4))