import math

class ConeCalculator:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.pi_value = 3.141592653589793

    def _get_base_area(self):
        return self.pi_value * (self.radius ** 2)

    def calculate_volume(self):
        base_area = self._get_base_area()
        return (base_area * self.height) / 3

    def get_radius(self):
        return self.radius

    def get_height(self):
        return self.height

if __name__ == '__main__':
    sample_radius = 7
    sample_height = 5
    cone_instance = ConeCalculator(sample_radius, sample_height)
    calculated_volume = cone_instance.calculate_volume()
    print(calculated_volume)
    print(cone_instance.get_radius())
    print(cone_instance.get_height())