VALID_EDGES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def cube_volume(edge):
    if not isinstance(edge, (int, float)):
        raise TypeError("Edge must be numeric")
    if edge < 0:
        raise ValueError("Edge must be non-negative")
    return edge * edge * edge

if __name__ == '__main__':
    test_edge = 4.5
    result = cube_volume(test_edge)
    print(result)