import math

class CircleAreaCalculator:
    def __init__(self):
        self.area_dict = {}

    def add_radius(self, radius):
        if not isinstance(radius, (int, float)):
            raise ValueError("Radius must be a number.")
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        area = math.pi * (radius ** 2)
        self.area_dict[radius] = area
        return area

    def get_areas(self):
        return self.area_dict

if __name__ == '__main__':
    calculator = CircleAreaCalculator()
    sample_radii = [1.0, 3.5, 6.2, 8.9]
    for radius in sample_radii:
        try:
            area = calculator.add_radius(radius)
            print(f"Radius: {radius}, Calculated Area: {area}")
        except ValueError as e:
            print(e)

    all_areas = calculator.get_areas()
    print("All calculated areas:", all_areas)