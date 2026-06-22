import math

class PyramidGeometry:
    @staticmethod
    def calculate_surface_area(base_side, slant_height):
        base_area = base_side * base_side
        triangular_face_area = 0.5 * base_side * slant_height
        lateral_area = 4 * triangular_face_area
        total_surface_area = base_area + lateral_area
        return total_surface_area

if __name__ == '__main__':
    result1 = PyramidGeometry.calculate_surface_area(4, 6)
    print(result1)

    result2 = PyramidGeometry.calculate_surface_area(10, 5)
    print(result2)

    result3 = PyramidGeometry.calculate_surface_area(2.5, 3.7)
    print(result3)