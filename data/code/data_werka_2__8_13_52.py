from typing import Union

class AreaCalculator:
    MIN_VALUE = 0.0

    @staticmethod
    def validate_input(value: float) -> None:
        if value < AreaCalculator.MIN_VALUE:
            raise ValueError("Base area and scale factor must be non-negative.")

    @staticmethod
    def calculate_scaled_area(base_area: Union[int, float], scale_factor: Union[int, float]) -> Union[int, float]:
        AreaCalculator.validate_input(base_area)
        AreaCalculator.validate_input(scale_factor)
        return base_area * (scale_factor ** 2)

if __name__ == '__main__':
    sample_base_area = 10.0
    sample_scale_factor = 3.0
    try:
        scaled_area = AreaCalculator.calculate_scaled_area(sample_base_area, sample_scale_factor)
        print(scaled_area)
    except ValueError as e:
        print(e)