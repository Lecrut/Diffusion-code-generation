from typing import Union

class Cube:
    def __init__(self, edge_length: Union[int, float]) -> None:
        if edge_length <= 0:
            raise ValueError("Edge length must be a positive number")
        self.edge_length = float(edge_length)

    def volume(self) -> float:
        return self.edge_length ** 3

def calculate_cube_volume(edge_length: Union[int, float]) -> float:
    if edge_length <= 0:
        raise ValueError("Edge length must be a positive number")
    return edge_length ** 3

if __name__ == '__main__':
    edge_1 = 3
    edge_2 = 5.5
    print(calculate_cube_volume(edge_1))
    cube_instance = Cube(edge_2)
    print(cube_instance.volume())