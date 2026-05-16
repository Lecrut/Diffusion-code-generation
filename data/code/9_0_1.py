import math
def convert_volume(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    conversion_factors = {
        'L': 1.0 / 1000.0,                       
        'mL': 1.0 / 1000.0,                            
        'm3': 1.0,
        'gal': 0.00378541,                                
        'in3': 0.0000163871,                                
        'm3': 1.0,
        'L': 1000.0,
        'mL': 1000.0,
        'gal': 264.172,                                
        'in3': 16387.1
    }
    value_in_m3 = value * conversion_factors.get(from_unit, 1.0)
    if to_unit == 'm3':
        return value_in_m3 / conversion_factors.get(to_unit, 1.0)
    result = value_in_m3 * conversion_factors.get(to_unit, 1.0)
    return result
def main():
    sample_value = 10.0
    from_unit = 'L'
    to_unit = 'gal'
    print(f"Sample Value: {sample_value} {from_unit}")
    conversions = {
        ('L', 'mL'): (sample_value * 1000.0),
        ('L', 'm3'): (sample_value / 1000.0),
        ('L', 'gal'): (sample_value / 3.78541),
        ('L', 'in3'): (sample_value * 61.0237),
        ('mL', 'm3'): (sample_value / 1000.0),
        ('mL', 'gal'): (sample_value * 0.00378541 / 1000.0),
        ('m3', 'L'): (sample_value * 1000.0),
        ('m3', 'gal'): (sample_value / 0.00378541),
        ('m3', 'in3'): (sample_value / 0.0000163871),
        ('gal', 'L'): (sample_value * 3.78541),
        ('gal', 'm3'): (sample_value * 0.00378541),
        ('gal', 'in3'): (sample_value * 264.172)
    }
    print("\n--- Hardcoded Sample Conversions ---")
    if (from_unit, to_unit) in conversions:
        result = conversions[(from_unit, to_unit)]
        print(f"{sample_value} {from_unit} is equal to {result:.4f} {to_unit}")
    else:
        print(f"Conversion from {from_unit} to {to_unit} is not directly pre-calculated in the sample set.")
    print("\n--- Demonstration of General Conversion Function ---")
    value = 500.0
    from_unit = 'mL'
    to_unit = 'm3'
    result = convert_volume(value, from_unit, to_unit)
    print(f"{value} {from_unit} is equal to {result:.6f} {to_unit}")
    value = 1.0
    from_unit = 'gal'
    to_unit = 'in3'
    result = convert_volume(value, from_unit, to_unit)
    print(f"{value} {from_unit} is equal to {result:.6f} {to_unit}")
if __name__ == '__main__':
    main()