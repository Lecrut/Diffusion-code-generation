import math

class Cone:
    def __init__(self, radius: float, height: float) -> None:
        self.radius = radius
        self.height = height

    def calculate_volume(self) -> float:
        return (1 / 3) * math.pi * self.radius ** 2 * self.height

if __name__ == '__main__':
    sample_radius = 5.0
    sample_height = 10.0
    cone_instance = Cone(sample_radius, sample_height)
    print(cone_instance.calculate_volume())