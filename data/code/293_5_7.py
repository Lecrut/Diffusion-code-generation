import math

class ShapeCalculator:
    PI = math.pi
    
    @staticmethod
    def calculate_volume(shape_type, dimensions):
        if shape_type == 'cube':
            side = dimensions[0]
            return side ** 3
        elif shape_type == 'cylinder':
            radius, height = dimensions
            return ShapeCalculator.PI * radius ** 2 * height
        elif shape_type == 'sphere':
            radius = dimensions[0]
            return (4/3) * ShapeCalculator.PI * radius ** 3
        else:
            raise ValueError("Invalid shape type")

if __name__ == '__main__':
    calculator = ShapeCalculator()
    print(calculator.calculate_volume('cube', [3]))
    print(calculator.calculate_volume('cylinder', [2, 5]))
    print(calculator.calculate_volume('sphere', [4]))