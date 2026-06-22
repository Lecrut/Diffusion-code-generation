def validate_side_length(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError("Side length must be a number")
    if side_length < 0:
        raise ValueError("Side length cannot be negative")

def calculate_square_area(side_length):
    validate_side_length(side_length)
    return side_length ** 2

class AreaCalculator:
    def __init__(self, shape_type, dimension):
        self.shape_type = shape_type
        self.dimension = dimension
        self.validate_dimension()

    def validate_dimension(self):
        if not isinstance(self.dimension, (int, float)):
            raise ValueError("Dimension must be a number")
        if self.dimension < 0:
            raise ValueError("Dimension cannot be negative")

    def calculate_area(self):
        if self.shape_type == 'square':
            return self.dimension ** 2
        else:
            raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    sample_side_length = 4
    area = calculate_square_area(sample_side_length)
    print(area)

    calculator = AreaCalculator('square', 6)
    area_from_calculator = calculator.calculate_area()
    print(area_from_calculator)