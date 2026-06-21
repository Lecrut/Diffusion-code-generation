import numpy as np

def convert_volumes(measurements, from_unit, to_unit):
    to_liters = {
        'liters': 1.0,
        'milliliters': 0.001,
        'gallons_us': 3.78541,
        'quarts_us': 0.946353,
        'pints_us': 0.473176,
        'cups_us': 0.236588,
        'fluid_ounces_us': 0.0295735,
        'cubic_meters': 1000.0,
        'cubic_inches': 0.0163871,
        'cubic_feet': 28.3168
    }
    
    if from_unit not in to_liters:
        raise ValueError(f"Unsupported unit: {from_unit}")
    if to_unit not in to_liters:
        raise ValueError(f"Unsupported unit: {to_unit}")
    
    factors_from = to_liters[from_unit]
    factors_to = to_liters[to_unit]
    
    measurements_array = np.asarray(measurements, dtype=np.float64)
    result = (measurements_array * factors_from) / factors_to
    
    return result

if __name__ == '__main__':
    sample_data = np.array([10.0, 50.0, 100.0, 1.5])
    converted = convert_volumes(sample_data, 'gallons_us', 'liters')
    print(converted)
    
    sample_data_2 = np.array([1000.0, 2500.0])
    converted_2 = convert_volumes(sample_data_2, 'liters', 'milliliters')
    print(converted_2)
    
    sample_data_3 = np.array([5.0])
    converted_3 = convert_volumes(sample_data_3, 'cubic_feet', 'cubic_meters')
    print(converted_3)