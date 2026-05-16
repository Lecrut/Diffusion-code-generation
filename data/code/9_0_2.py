import math
def convert_volume(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    conversion_factors = {
        'L': 1.0,
        'mL': 0.001,
        'm^3': 1000.0,
        'gal': 3.78541,
        'in^3': 0.0163871
    }
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Invalid unit specified.")
    value_in_liters = value * conversion_factors.get(from_unit, 1.0)
    result = value_in_liters / conversion_factors.get(to_unit, 1.0)
    return result
def main():
    sample_value = 10
    from_unit = 'L'
    to_unit = 'gal'
    print(f"Sample Value: {sample_value} {from_unit}")
    try:
        result = convert_volume(sample_value, from_unit, to_unit)
        print(f"Converted Value: {result:.4f} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}")
    sample_value_2 = 500
    from_unit_2 = 'm^3'
    to_unit_2 = 'mL'
    print(f"\nSample Value: {sample_value_2} {from_unit_2}")
    try:
        result_2 = convert_volume(sample_value_2, from_unit_2, to_unit_2)
        print(f"Converted Value: {result_2:.2f} {to_unit_2}")
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == '__main__':
    main()