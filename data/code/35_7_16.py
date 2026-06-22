def cube_volume(edge_length):
    if not isinstance(edge_length, (int, float)):
        raise TypeError('Edge length must be a number.')
    if edge_length < 0:
        raise ValueError('Edge length must be non-negative.')
    return edge_length ** 3
if __name__ == '__main__':
    sample_edge_lengths = [3, 5.5, 0, 10]
    for edge in sample_edge_lengths:
        volume = cube_volume(edge)
        print(volume)