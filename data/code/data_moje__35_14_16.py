def cube_volume(edge_length: float) -> float:
    if edge_length < 0:
        raise ValueError("Edge length must be non-negative")
    return edge_length ** 3

if __name__ == '__main__':
    sample_edge = 5.0
    result = cube_volume(sample_edge)
    print(result)