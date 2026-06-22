def calculate_cube_volume(edge_length):
    if edge_length < 0:
        raise ValueError("Edge length cannot be negative")
    return edge_length ** 3

if __name__ == '__main__':
    sample_edge = 5
    volume = calculate_cube_volume(sample_edge)
    print(volume)