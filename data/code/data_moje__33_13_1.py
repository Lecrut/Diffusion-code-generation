from dataclasses import dataclass

@dataclass
class TriangleGeometry:
    base: float
    height: float

    def area(self):
        return (self.base * self.height) / 2

if __name__ == '__main__':
    geometry = TriangleGeometry(base=10.0, height=5.0)
    print(geometry.area())