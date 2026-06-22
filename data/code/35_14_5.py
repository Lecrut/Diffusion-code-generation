def calculate_cube_volume(edge_length):
    if edge_length <= 0:
        raise ValueError("Edge length must be positive")
    return edge_length ** 3

if __name__ == '__main__':
    edge = 5
    volume = calculate_cube_volume(edge)
    print(volume)