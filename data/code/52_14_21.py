SQUARE_PROPERTIES = {'shape': 'square', 'dimension': 1}

def calculate_area(length):
    if length < 0:
        raise ValueError('Length cannot be negative')
    return length ** 2

class ShapeAreaCalculator:

    def __init__(self, properties):
        self.properties = properties

    def calculate_square_area(self):
        side_length = self.properties.get('dimension', 0)
        return calculate_area(side_length)
if __name__ == '__main__':
    sample_side_length = 7
    SQUARE_PROPERTIES['dimension'] = sample_side_length
    calculator = ShapeAreaCalculator(SQUARE_PROPERTIES)
    area = calculator.calculate_square_area()
    print(area)