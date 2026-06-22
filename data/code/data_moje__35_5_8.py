def cube_volume(edge):
    if not isinstance(edge, (int, float)):
        raise TypeError("Edge length must be a number")
    if edge < 0:
        raise ValueError("Edge length cannot be negative")
    return edge * edge * edge

if __name__ == '__main__':
    sample_edge = 6
    print(cube_volume(sample_edge))