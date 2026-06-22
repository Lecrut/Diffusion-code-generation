from typing import Tuple

class TriangleCalculator:
    AREA_MULTIPLIER = 0.5
    MINIMUM_DIMENSION = 1e-9

    @staticmethod
    def _validate_dimensions(base: float, height: float) -> Tuple[float, float]:
        if base < TriangleCalculator.MINIMUM_DIMENSION:
            raise ValueError("Base must be positive")
        if height < TriangleCalculator.MINIMUM_DIMENSION:
            raise ValueError("Height must be positive")
        return float(base), float(height)

    @staticmethod
    def compute_area(base: float, height: float) -> float:
        validated_base, validated_height = TriangleCalculator._validate_dimensions(base, height)
        return TriangleCalculator.AREA_MULTIPLIER * validated_base * validated_height

if __name__ == '__main__':
    base_value = 12.5
    height_value = 8.2
    computed_area = TriangleCalculator.compute_area(base_value, height_value)
    print(computed_area)