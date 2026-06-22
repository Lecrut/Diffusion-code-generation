from typing import Union

Number = Union[int, float]

def compute_cube_volume(edge_length: Number) -> Number:
    if edge_length < 0:
        raise ValueError("Edge length cannot be negative")
    return edge_length ** 3

if __name__ == '__main__':
    sample_edge = 5
    volume = compute_cube_volume(sample_edge)
    print(volume)
    print(compute_cube_volume(10))
    print(compute_cube_volume(2.5))