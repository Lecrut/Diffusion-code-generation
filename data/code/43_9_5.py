class SurfaceAreaCalculator:
    @staticmethod
    def calculate_square_pyramid_surface_area(base_side, slant_height):
        base_area = base_side ** 2
        lateral_area = 2 * base_side * slant_height
        return base_area + lateral_area

if __name__ == '__main__':
    base_side_1 = 10
    slant_height_1 = 12
    result_1 = SurfaceAreaCalculator.calculate_square_pyramid_surface_area(base_side_1, slant_height_1)
    print(result_1)
    base_side_2 = 5.5
    slant_height_2 = 8.0
    result_2 = SurfaceAreaCalculator.calculate_square_pyramid_surface_area(base_side_2, slant_height_2)
    print(result_2)