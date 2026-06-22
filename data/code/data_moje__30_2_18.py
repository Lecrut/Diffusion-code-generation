import math

class CircleCalculator:
    def __init__(self, radius: float) -> None:
        self.radius = radius
        self.pi_constant = math.pi

    def compute_area(self) -> float:
        if self.radius < 0:
            raise ValueError("Radius cannot be negative")
        return self.pi_constant * (self.radius ** 2)

    def get_radius(self) -> float:
        return self.radius

if __name__ == '__main__':
    radius_input = 7.5
    circle_instance = CircleCalculator(radius_input)
    area_result = circle_instance.compute_area()
    print(area_result)
    print(circle_instance.get_radius())