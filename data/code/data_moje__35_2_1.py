from typing import Union

Number = Union[int, float]

def compute_cube_volume(edge_length: Number) -> Number:
    if edge_length < 0:
        raise ValueError("Edge length must be non-negative")
    return edge_length ** 3

if __name__ == '__main__':
    sample_edge = 5
    print(compute_cube_volume(sample_edge))
    sample_edge_float = 2.5
    print(compute_cube_volume(sample_edge_float))