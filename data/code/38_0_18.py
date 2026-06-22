import math

class Cone:
    def __init__(self, radius: float, height: float) -> None:
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        if height < 0:
            raise ValueError("Height cannot be negative")
        self.radius = radius
        self.height = height

    def calculate_volume(self) -> float:
        base_area = math.pi * (self.radius ** 2)
        return (1.0 / 3.0) * base_area * self.height

if __name__ == '__main__':
    test_radius = 7.5
    test_height = 14.2
    cone = Cone(test_radius, test_height)
    print(cone.calculate_volume())