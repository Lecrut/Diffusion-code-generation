def compute_cube_volume(edge_length):
    if edge_length < 0:
        raise ValueError("Edge length must be non-negative")
    return edge_length ** 3

if __name__ == '__main__':
    edge_length = 5
    volume = compute_cube_volume(edge_length)
    print(volume)