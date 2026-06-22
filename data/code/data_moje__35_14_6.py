def cube_volume(edge_length: float) -> float:
    if edge_length < 0:
        raise ValueError("Edge length must be non-negative")
    return edge_length ** 3

if __name__ == '__main__':
    print(cube_volume(5))
    print(cube_volume(3.0))
    print(cube_volume(0))