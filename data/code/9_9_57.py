from typing import Union

def liters_to_gallons(liters: float) -> float:
    return liters * 0.264172

def gallons_to_liters(gallons: float) -> float:
    return gallons / 0.264172

def cubic_meters_to_liters(cubic_meters: float) -> float:
    return cubic_meters * 1000

def liters_to_cubic_meters(liters: float) -> float:
    return liters / 1000

def milliliters_to_liters(milliliters: float) -> float:
    return milliliters / 1000

def liters_to_milliliters(liters: float) -> float:
    return liters * 1000

def convert_volume(value: Union[float, int], from_unit: str, to_unit: str) -> float:
    if from_unit == 'L' and to_unit == 'gal':
        return liters_to_gallons(value)
    elif from_unit == 'gal' and to_unit == 'L':
        return gallons_to_liters(value)
    elif from_unit == 'm³' and to_unit == 'L':
        return cubic_meters_to_liters(value)
    elif from_unit == 'L' and to_unit == 'm³':
        return liters_to_cubic_meters(value)
    elif from_unit == 'mL' and to_unit == 'L':
        return milliliters_to_liters(value)
    elif from_unit == 'L' and to_unit == 'mL':
        return liters_to_milliliters(value)
    else:
        raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    sample_values = [
        (10, 'L', 'gal'),
        (5, 'gal', 'L'),
        (2, 'm³', 'L'),
        (1500, 'L', 'm³'),
        (300, 'mL', 'L'),
        (2.5, 'L', 'mL')
    ]

    for value, from_unit, to_unit in sample_values:
        converted_value = convert_volume(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {converted_value:.4f} {to_unit}")