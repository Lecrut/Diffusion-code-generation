def convert_volume(value: float, from_unit: str, to_unit: str) -> float:
    conversion_to_liters = {'L': 1.0, 'mL': 0.001, 'm3': 1000.0, 'gal': 3.78541}
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    if from_unit_lower not in conversion_to_liters:
        raise ValueError(f'Unsupported from_unit: {from_unit}')
    if to_unit_lower not in conversion_to_liters:
        raise ValueError(f'Unsupported to_unit: {to_unit}')
    liters = value * conversion_to_liters[from_unit_lower]
    result = liters / conversion_to_liters[to_unit_lower]
    return result

def liters_to_milliliters(liters: float) -> float:
    return convert_volume(liters, 'L', 'mL')

def milliliters_to_liters(milliliters: float) -> float:
    return convert_volume(milliliters, 'mL', 'L')

def cubic_meters_to_liters(cubic_meters: float) -> float:
    return convert_volume(cubic_meters, 'm3', 'L')

def liters_to_gallons(liters: float) -> float:
    return convert_volume(liters, 'L', 'gal')

def gallons_to_liters(gallons: float) -> float:
    return convert_volume(gallons, 'gal', 'L')

def cubic_meters_to_gallons(cubic_meters: float) -> float:
    return convert_volume(cubic_meters, 'm3', 'gal')

def gallons_to_cubic_meters(gallons: float) -> float:
    return convert_volume(gallons, 'gal', 'm3')

def milliliters_to_gallons(milliliters: float) -> float:
    return convert_volume(milliliters, 'mL', 'gal')

def gallons_to_milliliters(gallons: float) -> float:
    return convert_volume(gallons, 'gal', 'mL')

def cubic_meters_to_milliliters(cubic_meters: float) -> float:
    return convert_volume(cubic_meters, 'm3', 'mL')

def milliliters_to_cubic_meters(milliliters: float) -> float:
    return convert_volume(milliliters, 'mL', 'm3')
if __name__ == '__main__':
    sample_liters = 2.5
    sample_milliliters = 500
    sample_cubic_meters = 1.0
    sample_gallons = 1.0
    print(f'{sample_liters} L to mL: {liters_to_milliliters(sample_liters)}')
    print(f'{sample_milliliters} mL to L: {milliliters_to_liters(sample_milliliters)}')
    print(f'{sample_cubic_meters} m³ to L: {cubic_meters_to_liters(sample_cubic_meters)}')
    print(f'{sample_liters} L to gal: {liters_to_gallons(sample_liters)}')
    print(f'{sample_gallons} gal to L: {gallons_to_liters(sample_gallons)}')
    print(f'{sample_cubic_meters} m³ to gal: {cubic_meters_to_gallons(sample_cubic_meters)}')
    print(f'{sample_gallons} gal to m³: {gallons_to_cubic_meters(sample_gallons)}')
    print(f'{sample_milliliters} mL to gal: {milliliters_to_gallons(sample_milliliters)}')
    print(f'{sample_gallons} gal to mL: {gallons_to_milliliters(sample_gallons)}')
    print(f'{sample_cubic_meters} m³ to mL: {cubic_meters_to_milliliters(sample_cubic_meters)}')
    print(f'{sample_milliliters} mL to m³: {milliliters_to_cubic_meters(sample_milliliters)}')
    print(f"Generic: {sample_liters} L to gal: {convert_volume(sample_liters, 'L', 'gal')}")
    print(f"Generic: {sample_gallons} gal to L: {convert_volume(sample_gallons, 'gal', 'L')}")