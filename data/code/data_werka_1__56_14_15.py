import math

class VolumeCalculator:
    def __init__(self):
        self.cube_edge_length = 3
        self.sphere_radius = 2

    def cube_volume(self):
        return self.cube_edge_length ** 3

    def sphere_volume(self):
        return (4/3) * math.pi * (self.sphere_radius ** 3)

    def compare_volumes(self):
        cube_vol = self.cube_volume()
        sphere_vol = self.sphere_volume()
        return cube_vol > sphere_vol

if __name__ == '__main__':
    calculator = VolumeCalculator()
    result = calculator.compare_volumes()
    print(result)