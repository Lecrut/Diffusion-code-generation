from typing import Dict

def calculate_scaled_area(base_area: float, scale_factor: float) -> float:
    if base_area < 0 or scale_factor < 0:
        raise ValueError('Base area and scale factor must be non-negative.')
    return base_area * scale_factor ** 2
if __name__ == '__main__':
    sample_values: Dict[str, float] = {'base_area': 12.5, 'scale_factor': 3.0}
    try:
        scaled_area = calculate_scaled_area(sample_values['base_area'], sample_values['scale_factor'])
        print(scaled_area)
    except ValueError as e:
        print(e)