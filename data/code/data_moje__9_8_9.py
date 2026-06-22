import numpy as np

def convert_volumes(volumes, from_unit='liter', to_unit='gallon'):
    conversion_to_liters = {'liter': 1.0, 'gallon': 3.78541, 'milliliter': 0.001, 'cubic_meter': 1000.0}
    from_factor = conversion_to_liters[from_unit.lower()]
    to_factor = conversion_to_liters[to_unit.lower()]
    volumes = np.asarray(volumes, dtype=float)
    converted = volumes * from_factor / to_factor
    return converted
if __name__ == '__main__':
    sample_volumes = np.array([1.0, 2.5, 10.0, 0.5, 100.0])
    liters_to_gallons = convert_volumes(sample_volumes, from_unit='liter', to_unit='gallon')
    print(liters_to_gallons)
    gallons_to_liters = convert_volumes(sample_volumes, from_unit='gallon', to_unit='liter')
    print(gallons_to_liters)
    ml_to_liters = convert_volumes(sample_volumes, from_unit='milliliter', to_unit='liter')
    print(ml_to_liters)
    cubic_meters_to_gallons = convert_volumes(sample_volumes, from_unit='cubic_meter', to_unit='gallon')
    print(cubic_meters_to_gallons)