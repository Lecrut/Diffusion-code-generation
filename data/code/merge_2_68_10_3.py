import re
def parse_volume_input(volume_str: str) -> float:
    if not isinstance(volume_str, str):
        raise TypeError("Input must be a string.")
    match = re.match(r'^([+-]?[0-9]*\.?[0-9]+)\s*(liters?|gallons?)$', volume_str.strip(), re.IGNORECASE)
    if not match:
        raise ValueError(f"Invalid input format. Expected 'X liters' or 'Y gallons'. Got '{volume_str}'.")
    value = float(match.group(1))
    unit = match.group(2).lower()
    return value, unit
def convert_volume(liters_value: float) -> dict:
    conversion_rate = 0.264172
    return {
        'liters': liters_value,
        'gallons': round(liters_value * conversion_rate, 2),
        'unit': 'gal'
    }
def convert_volume_gal(gallons_value: float) -> dict:
    conversion_rate = 3.78541
    return {
        'liters': round(gallons_value * conversion_rate, 2),
        'gallons': gallons_value,
        'unit': 'L'
    }
def format_output(result: dict) -> str:
    if result['unit'] == 'gal':
        return f"{result['liters']} liters = {result['gallons']} gallons"
    else:
        return f"{result['gallons']} gallons = {result['liters']} liters"
if __name__ == '__main__':
    sample_inputs = [
        "5.2 liters",
        "10.5 gallons",
        "-3.7 liters",
        "0 liters",
        "invalid input"                             
    ]
    for item in sample_inputs:
        try:
            val, unit = parse_volume_input(item)
            if unit.endswith('liter'):
                result = convert_volume(val)
                print(f"Input: {item}")
                print(format_output(result))
            elif unit.endswith('gallon'):
                result = convert_volume_gal(val)
                print(f"Input: {item}")
                print(format_output(result))
        except (ValueError, TypeError) as e:
            print(f"Input: {item} -> Error: {e}")