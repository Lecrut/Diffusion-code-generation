import math

class ShapeCalculator:

    @staticmethod
    def square_pyramid_surface_area(base_edge: float, slant_height: float) -> float:
        base_area = base_edge ** 2
        lateral_area = 2 * base_edge * slant_height
        return base_area + lateral_area

if __name__ == '__main__':
    base_edge = 10
    slant_height = 12
    calculator = ShapeCalculator()
    result = calculator.square_pyramid_surface_area(base_edge, slant_height)
    print(result)