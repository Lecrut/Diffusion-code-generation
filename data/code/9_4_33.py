import argparse

def convert_volume(volume, from_unit, to_unit):
    conversion_factors = {
        'm3': {'m3': 1, 'cm3': 1000000, 'liters': 1000},
        'cm3': {'m3': 0.000001, 'cm3': 1, 'liters': 1},
        'liters': {'m3': 0.001, 'cm3': 1, 'liters': 1}
    }
    
    if from_unit not in conversion_factors or to_unit not in conversion_factors[from_unit]:
        raise ValueError("Invalid unit conversion")
    
    return volume * conversion_factors[from_unit][to_unit]

if __name__ == '__main__':
    sample_volume = 5
    sample_from_unit = 'm3'
    sample_to_unit = 'liters'
    
    result = convert_volume(sample_volume, sample_from_unit, sample_to_unit)
    print(result)