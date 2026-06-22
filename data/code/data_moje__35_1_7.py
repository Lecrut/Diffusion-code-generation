def cube_volume(edge: float) -> float:
    return edge ** 3

if __name__ == '__main__':
    edge_length = 3.0
    result = cube_volume(edge_length)
    print(result)