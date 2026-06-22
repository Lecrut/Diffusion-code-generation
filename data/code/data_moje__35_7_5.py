def calculate_cube_volume(edge_length):
    if edge_length < 0:
        raise ValueError("Edge length must be non-negative")
    return edge_length ** 3

if __name__ == '__main__':
    sample_edges = [3.0, 5.5, 0.0, 10.25]
    for edge in sample_edges:
        volume = calculate_cube_volume(edge)
        print(f"Edge: {edge}, Volume: {volume}")