def calculate_cube_volume(edge_length):
    if edge_length < 0:
        raise ValueError("Edge length cannot be negative")
    return edge_length ** 3

if __name__ == '__main__':
    sample_edge_lengths = [2, 5, 7.5]
    for length in sample_edge_lengths:
        volume = calculate_cube_volume(length)
        print(volume)