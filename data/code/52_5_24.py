from typing import Union

class AreaCalculator:
    MIN_DIMENSION = 0

    @staticmethod
    def calculate_area(length: Union[int, float], width: Union[int, float]) -> Union[int, float]:
        if length < AreaCalculator.MIN_DIMENSION or width < AreaCalculator.MIN_DIMENSION:
            raise ValueError("Length and width must be non-negative numbers.")
        return length * width

if __name__ == '__main__':
    sample_length = 6.0
    sample_width = 2.5
    area_calculator = AreaCalculator()
    calculated_area = area_calculator.calculate_area(sample_length, sample_width)
    print(calculated_area)