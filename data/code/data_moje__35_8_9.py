def volume_of_cube(edge_length):
    if edge_length < 0:
        raise ValueError("Edge length cannot be negative")
    if not isinstance(edge_length, (int, float)):
        raise TypeError("Edge length must be a number")
    return edge_length * edge_length * edge_length

if __name__ == '__main__':
    test_edge = 6.0
    computed_volume = volume_of_cube(test_edge)
    print(computed_volume)