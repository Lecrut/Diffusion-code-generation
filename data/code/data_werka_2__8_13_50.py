from typing import Union

def calculate_scaled_area(base_area: float, scale_factor: float) -> float:
    if base_area < 0 or scale_factor < 0:
        raise ValueError("Base area and scale factor must be non-negative.")
    
    scaled_factor = scale_factor ** 2
    result_area = base_area * scaled_factor
    return result_area

if __name__ == '__main__':
    sample_base_area = 15.0
    sample_scale_factor = 2.0
    
    try:
        area_result = calculate_scaled_area(sample_base_area, sample_scale_factor)
        print(area_result)
    except ValueError as e:
        print(e)