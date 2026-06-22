from typing import Union

Number = Union[int, float]

def validate_dimensions(width: Number, height: Number) -> None:
    if width <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive")

def calculate_area(width: Number, height: Number) -> Number:
    validate_dimensions(width, height)
    return float(width) * float(height)

class RectangleCalculator:
    def __init__(self, width: Number, height: Number) -> None:
        self.width = width
        self.height = height

    def get_area(self) -> Number:
        validate_dimensions(self.width, self.height)
        return self.width * self.height

if __name__ == '__main__':
    sample_width = 12.5
    sample_height = 8.0
    direct_result = calculate_area(sample_width, sample_height)
    print(direct_result)
    
    rect_instance = RectangleCalculator(sample_width, sample_height * 2)
    print(rect_instance.get_area())