from typing import Union

class AreaCalculator:
    MIN_VALID_VALUE = 0.0

    @staticmethod
    def validate_value(value: Union[int, float]) -> None:
        if value < AreaCalculator.MIN_VALID_VALUE:
            raise ValueError("Base area and scale factor must be non-negative.")

    @staticmethod
    def calculate_scaled_area(base_area: Union[int, float], scale_factor: Union[int, float]) -> Union[int, float]:
        AreaCalculator.validate_value(base_area)
        AreaCalculator.validate_value(scale_factor)
        return base_area * (scale_factor ** 2)

if __name__ == '__main__':
    sample_base_area = 12.0
    sample_scale_factor = 3.5
    scaled_area = AreaCalculator.calculate_scaled_area(sample_base_area, sample_scale_factor)
    print(scaled_area)