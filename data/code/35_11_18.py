from typing import Union

class Cube:
    def __init__(self, edge_length: float) -> None:
        if edge_length <= 0:
            raise ValueError("Edge length must be a positive number")
        self.edge_length = edge_length

    def calculate_volume(self) -> float:
        return self.edge_length ** 3

def calculate_cube_volume(edge_length: float) -> float:
    if edge_length <= 0:
        raise ValueError("Edge length must be a positive number")
    return edge_length ** 3

if __name__ == "__main__":
    sample_edge = 4.5
    volume = calculate_cube_volume(sample_edge)
    print(volume)

    cube_instance = Cube(3)
    instance_volume = cube_instance.calculate_volume()
    print(instance_volume)