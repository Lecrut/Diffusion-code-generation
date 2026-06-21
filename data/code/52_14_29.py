SQUARE_CONFIG = {'type': 'square', 'side_length': 0}

def validate_side_length(length):
    if not isinstance(length, (int, float)):
        raise ValueError("Side length must be a number")
    if length < 0:
        raise ValueError("Side length cannot be negative")

def calculate_area(config):
    side_length = config.get('side_length', 0)
    validate_side_length(side_length)
    return side_length ** 2

class AreaCalculator:
    def __init__(self, config):
        self.config = config
    def compute_square_area(self):
        return calculate_area(self.config)

if __name__ == '__main__':
    sample_side_length = 4
    SQUARE_CONFIG['side_length'] = sample_side_length
    area_calculator = AreaCalculator(SQUARE_CONFIG)
    area = area_calculator.compute_square_area()
    print(area)