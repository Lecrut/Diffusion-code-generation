import math

class GeometryUtils:
    @staticmethod
    def square_pyramid_surface_area(base_side: float, slant_height: float) -> float:
        base_area = base_side * base_side
        lateral_area = 2 * base_side * slant_height
        return base_area + lateral_area

if __name__ == '__main__':
    result = GeometryUtils.square_pyramid_surface_area(10, 12)
    print(result)