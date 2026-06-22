class Cube:
    def __init__(self, edge_length: float) -> None:
        self.edge_length = edge_length

    def volume(self) -> float:
        if self.edge_length <= 0:
            return 0.0
        return self.edge_length * self.edge_length * self.edge_length

if __name__ == '__main__':
    edge_values = [4.0, 0.5, 10]
    for val in edge_values:
        cube = Cube(val)
        print(cube.volume())