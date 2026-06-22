from typing import Union

Number = Union[int, float]

def cube_volume(edge_length: Number) -> Number:
    if edge_length < 0:
        raise ValueError("Edge length cannot be negative")
    return edge_length ** 3

if __name__ == "__main__":
    sample_edge: Number = 3
    result = cube_volume(sample_edge)
    print(result)