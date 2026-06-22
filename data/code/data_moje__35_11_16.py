from typing import Union
from math import isclose

class Cube:
    def __init__(self, edge_length: Union[int, float]):
        if edge_length <= 0:
            raise ValueError("Edge length must be positive")
        if not isinstance(edge_length, (int, float)):
            raise TypeError("Edge length must be a number")
        self.edge_length = edge_length

    def calculate_volume(self) -> Union[int, float]:
        return self.edge_length ** 3

if __name__ == '__main__':
    cube_one = Cube(3)
    print(cube_one.calculate_volume())

    cube_two = Cube(5.5)
    print(cube_two.calculate_volume())