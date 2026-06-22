from typing import Union

def calculate_cube_volume(edge: Union[int, float]) -> float:
    if not isinstance(edge, (int, float)):
        raise TypeError("Edge length must be a number.")
    if edge < 0:
        raise ValueError("Edge length cannot be negative.")
    return float(edge ** 3)

if __name__ == '__main__':
    edge_length = 5.0
    volume = calculate_cube_volume(edge_length)
    print(volume)