import math

class VolumeCalculator:
    def __init__(self, cube_edge=3, sphere_radius=2):
        self.cube_edge = cube_edge
        self.sphere_radius = sphere_radius

    def calculate_cube_volume(self):
        return self.cube_edge ** 3

    def calculate_sphere_volume(self):
        return (4/3) * math.pi * (self.sphere_radius ** 3)

    def is_cube_volume_greater(self):
        cube_volume = self.calculate_cube_volume()
        sphere_volume = self.calculate_sphere_volume()
        return cube_volume > sphere_volume

if __name__ == '__main__':
    volume_calculator = VolumeCalculator()
    cube_volume = volume_calculator.calculate_cube_volume()
    sphere_volume = volume_calculator.calculate_sphere_volume()
    is_greater = volume_calculator.is_cube_volume_greater()

    print("Cube Volume:", cube_volume)
    print("Sphere Volume:", sphere_volume)
    print("Is Cube Volume Greater?", is_greater)