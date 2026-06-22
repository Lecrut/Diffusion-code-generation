import math

class ShapeVolumeCalculator:
    def calculate_volume(self, shape_type, dimensions):
        if shape_type == 'cube':
            side = dimensions[0]
            return side ** 3
        elif shape_type == 'cylinder':
            radius, height = dimensions
            return math.pi * radius ** 2 * height
        elif shape_type == 'sphere':
            radius = dimensions[0]
            return (4/3) * math.pi * radius ** 3
        else:
            raise ValueError("Invalid shape type")

if __name__ == '__main__':
    calculator = ShapeVolumeCalculator()
    cube_volume = calculator.calculate_volume('cube', [2])
    cylinder_volume = calculator.calculate_volume('cylinder', [3, 7])
    sphere_volume = calculator.calculate_volume('sphere', [5])

    print(f"Cube Volume: {cube_volume}")
    print(f"Cylinder Volume: {cylinder_volume}")
    print(f"Sphere Volume: {sphere_volume}")