from typing import Union
CONVERSION_FACTORS = {('L', 'mL'): 1000, ('mL', 'L'): 1 / 1000, ('L', 'gal'): 0.264172, ('gal', 'L'): 1 / 0.264172, ('m³', 'L'): 1000, ('L', 'm³'): 1 / 1000}

def convert_volume(value: Union[float, int], from_unit: str, to_unit: str) -> float:
    if (from_unit, to_unit) in CONVERSION_FACTORS:
        return value * CONVERSION_FACTORS[from_unit, to_unit]
    else:
        raise ValueError(f'Conversion from {from_unit} to {to_unit} is not supported.')
if __name__ == '__main__':
    sample_liters = 5.0
    sample_milliliters = 1500.0
    sample_cubic_meters = 0.003
    sample_gallons = 1.0
    print(convert_volume(sample_liters, 'L', 'mL'))
    print(convert_volume(sample_milliliters, 'mL', 'L'))
    print(convert_volume(sample_cubic_meters, 'm³', 'L'))
    print(convert_volume(sample_liters, 'L', 'gal'))
    print(convert_volume(sample_gallons, 'gal', 'L'))