from typing import Union

def compute_cube_volume(edge_length: Union[int, float]) -> Union[int, float]:
    return edge_length ** 3

if __name__ == '__main__':
    sample_edge = 4
    result = compute_cube_volume(sample_edge)
    print(result)