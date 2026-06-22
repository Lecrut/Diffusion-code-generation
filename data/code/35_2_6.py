def cube_volume(edge_length: float) -> float:
    return edge_length ** 3

if __name__ == '__main__':
    edge: float = 5.0
    volume: float = cube_volume(edge)
    print(volume)