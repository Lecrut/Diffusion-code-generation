class GeometryCalculator:
    def calculate_area(self, shape, dimension):
        if shape == 'circle':
            return 3.14159 * (dimension ** 2)
        elif shape == 'square':
            return dimension ** 2
        else:
            raise ValueError("Unsupported shape")

def sum_areas(circle_radius, square_side):
    calculator = GeometryCalculator()
    circle_area = calculator.calculate_area('circle', circle_radius)
    square_area = calculator.calculate_area('square', square_side)
    return circle_area + square_side

if __name__ == '__main__':
    total_area = sum_areas(3, 4)
    print(total_area)