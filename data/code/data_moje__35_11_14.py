from typing import Union

def calculate_cube_volume(edge_length: Union[int, float]) -> float:
    if not isinstance(edge_length, (int, float)):
        raise TypeError("Edge length must be a number.")
    if edge_length <= 0:
        raise ValueError("Edge length must be positive.")
    return edge_length ** 3

if __name__ == '__main__':
    result = calculate_cube_volume(5)
    print(result)