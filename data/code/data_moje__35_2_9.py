from typing import Union

Number = Union[int, float]

def cube_volume(edge_length: Number) -> Number:
    if edge_length < 0:
        raise ValueError("Edge length must be non-negative")
    return edge_length ** 3

if __name__ == '__main__':
    sample_edge = 5.0
    volume = cube_volume(sample_edge)
    print(volume)