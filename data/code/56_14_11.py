import math

class VolumeCalculator:
    def calculate_cube_volume(self, edge_length):
        return edge_length ** 3

    def calculate_sphere_volume(self, radius):
        return (4/3) * math.pi * (radius ** 3)

    def compare_volumes(self, cube_edge, sphere_radius):
        cube_volume = self.calculate_cube_volume(cube_edge)
        sphere_volume = self.calculate_sphere_volume(sphere_radius)
        return cube_volume > sphere_volume

if __name__ == '__main__':
    calculator = VolumeCalculator()
    cube_edge_length = 3
    sphere_radius = 2
    comparison_result = calculator.compare_volumes(cube_edge_length, sphere_radius)
    print(comparison_result)