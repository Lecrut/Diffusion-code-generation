class Cube:
    def __init__(self, edge_length: float) -> None:
        if edge_length < 0:
            raise ValueError("Edge length must be non-negative")
        self.edge_length = edge_length

    def volume(self) -> float:
        return self.edge_length ** 3

if __name__ == "__main__":
    cube = Cube(5)
    print(cube.volume())