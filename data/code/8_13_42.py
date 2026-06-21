from typing import Union

class AreaCalculator:
    def __init__(self, base_area: float):
        if base_area < 0:
            raise ValueError("Base area must be non-negative.")
        self.base_area = base_area

    def calculate_scaled_area(self, scale_factor: float) -> float:
        if scale_factor < 0:
            raise ValueError("Scale factor must be non-negative.")
        return self.base_area * (scale_factor ** 2)

if __name__ == '__main__':
    sample_base_area = 12.5
    area_calculator = AreaCalculator(sample_base_area)
    
    sample_scale_factor_1 = 3.0
    scaled_area_1 = area_calculator.calculate_scaled_area(sample_scale_factor_1)
    print(f"Scaled Area with scale factor {sample_scale_factor_1}: {scaled_area_1}")
    
    sample_scale_factor_2 = 4.5
    scaled_area_2 = area_calculator.calculate_scaled_area(sample_scale_factor_2)
    print(f"Scaled Area with scale factor {sample_scale_factor_2}: {scaled_area_2}")