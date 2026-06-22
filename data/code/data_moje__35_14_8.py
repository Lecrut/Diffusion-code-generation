from dataclasses import dataclass

DIMENSION = 3

@dataclass
class Cube:
    edge_length: float

    def volume(self):
        if self.edge_length < 0:
            raise ValueError("Edge length must be non-negative")
        return self.edge_length ** DIMENSION

if __name__ == '__main__':
    cube1 = Cube(4)
    print(cube1.volume())
    cube2 = Cube(2.5)
    print(cube2.volume())