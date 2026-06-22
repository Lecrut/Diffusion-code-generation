def calculate_cube_volume(edge_length):
    if edge_length < 0:
        raise ValueError("Edge length cannot be negative")
    return edge_length ** 3

if __name__ == '__main__':
    values = [2.0, 3.5, 4.125]
    for val in values:
        print(calculate_cube_volume(val))