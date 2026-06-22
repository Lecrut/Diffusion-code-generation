class Cube:
    def __init__(self, edge_length: float) -> None:
        if not isinstance(edge_length, (int, float)):
            raise TypeError("Edge length must be a number")
        if edge_length < 0:
            raise ValueError("Edge length must be non-negative")
        self._edge = float(edge_length)

    def get_volume(self) -> float:
        return self._edge ** 3

if __name__ == '__main__':
    cube = Cube(5)
    print(cube.get_volume())