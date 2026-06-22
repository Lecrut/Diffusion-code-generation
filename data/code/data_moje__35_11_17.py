from typing import Union

def calculate_cube_volume(edge_length: Union[int, float]) -> float:
    if not isinstance(edge_length, (int, float)):
        raise TypeError("Edge length must be a number.")
    if edge_length < 0:
        raise ValueError("Edge length cannot be negative.")
    return float(edge_length ** 3)

if __name__ == '__main__':
    sample_edge_1 = 3
    sample_edge_2 = 2.5
    result_1 = calculate_cube_volume(sample_edge_1)
    result_2 = calculate_cube_volume(sample_edge_2)
    print(result_1)
    print(result_2)