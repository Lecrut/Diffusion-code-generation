from typing import Union

Number = Union[int, float]

def volume_of_cube(edge_length: Number) -> Number:
    return edge_length ** 3

if __name__ == '__main__':
    print(volume_of_cube(3))
    print(volume_of_cube(5.5))