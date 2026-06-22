def calculate_cube_volume(edge_length: float) -> float:
    if edge_length < 0:
        raise ValueError("Edge length must be non-negative")
    return edge_length ** 3

if __name__ == '__main__':
    sample_edges = [3.0, 5.5, 0.0, -2.0]
    for edge in sample_edges:
        try:
            volume = calculate_cube_volume(edge)
            print(f"Edge: {edge}, Volume: {volume}")
        except ValueError as e:
            print(f"Error: {e}")