SQUARE_ATTRIBUTES = {'shape': 'square', 'side_length': 0}

def calculate_area(attributes):
    side_length = attributes.get('side_length')
    if not isinstance(side_length, (int, float)):
        raise ValueError("Side length must be a number")
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length ** 2

class AreaCalculator:
    def __init__(self, attributes):
        self.attributes = attributes
    def calculate_square_area(self):
        return calculate_area(self.attributes)

if __name__ == '__main__':
    sample_side_length = 4
    SQUARE_ATTRIBUTES['side_length'] = sample_side_length
    calculator = AreaCalculator(SQUARE_ATTRIBUTES)
    area = calculator.calculate_square_area()
    print(area)

    another_sample_side_length = 10
    SQUARE_ATTRIBUTES['side_length'] = another_sample_side_length
    another_calculator = AreaCalculator(SQUARE_ATTRIBUTES)
    another_area = another_calculator.calculate_square_area()
    print(another_area)