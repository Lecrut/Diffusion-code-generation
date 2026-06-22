def cube_volume(edge_length: float) -> float:
    return edge_length ** 3

if __name__ == '__main__':
    edge = 5.0
    volume = cube_volume(edge)
    print(volume)