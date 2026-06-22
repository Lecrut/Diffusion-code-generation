from typing import Union

def calculate_cube_volume(edge_length: Union[int, float]) -> Union[int, float]:
    if not isinstance(edge_length, (int, float)):
        raise TypeError("Edge length must be a number")
    if edge_length < 0:
        raise ValueError("Edge length must be non-negative")
    return edge_length ** 3

if __name__ == '__main__':
    sample_edge = 3
    result = calculate_cube_volume(sample_edge)
    print(result)