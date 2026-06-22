from dataclasses import dataclass

DIMENSION = "3D"

@dataclass
class CubeGeometry:
    edge_length: float

    def get_volume(self) -> float:
        return self.edge_length ** 3

    def get_dimension_name(self) -> str:
        return DIMENSION

if __name__ == '__main__':
    edge_value = 4
    shape = CubeGeometry(edge_value)
    computed_volume = shape.get_volume()
    dimension = shape.get_dimension_name()
    print(computed_volume)
    print(dimension)