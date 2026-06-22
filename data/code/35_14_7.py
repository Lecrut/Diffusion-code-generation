def calculate_cube_volume(edge_length):
    if edge_length < 0:
        raise ValueError("Edge length cannot be negative")
    return edge_length ** 3

if __name__ == "__main__":
    sample_edge = 5
    result = calculate_cube_volume(sample_edge)
    print(result)

    sample_edge_negative = -3
    try:
        result_negative = calculate_cube_volume(sample_edge_negative)
        print(result_negative)
    except ValueError as e:
        print(str(e))

    sample_edge_zero = 0
    print(calculate_cube_volume(sample_edge_zero))