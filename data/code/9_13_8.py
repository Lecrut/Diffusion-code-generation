def liters_to_milliliters(liters: float) -> float:
    return liters * 1000.0

def milliliters_to_liters(milliliters: float) -> float:
    return milliliters / 1000.0

def cubic_meters_to_liters(cubic_meters: float) -> float:
    return cubic_meters * 1000.0

def liters_to_cubic_meters(liters: float) -> float:
    return liters / 1000.0

def liters_to_gallons(liters: float) -> float:
    return liters * 0.264172

def gallons_to_liters(gallons: float) -> float:
    return gallons / 0.264172

def convert_volume(value: float, from_unit: str, to_unit: str) -> float:
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == to_unit:
        return value

    conversions = {
        ('l', 'ml'): liters_to_milliliters,
        ('ml', 'l'): milliliters_to_liters,
        ('m3', 'l'): cubic_meters_to_liters,
        ('l', 'm3'): liters_to_cubic_meters,
        ('l', 'gal'): liters_to_gallons,
        ('gal', 'l'): gallons_to_liters,
        ('m3', 'ml'): lambda x: liters_to_milliliters(cubic_meters_to_liters(x)),
        ('ml', 'm3'): lambda x: liters_to_cubic_meters(milliliters_to_liters(x)),
        ('gal', 'ml'): lambda x: liters_to_milliliters(gallons_to_liters(x)),
        ('ml', 'gal'): lambda x: gallons_to_liters(milliliters_to_liters(x)),
        ('gal', 'm3'): lambda x: liters_to_cubic_meters(gallons_to_liters(x)),
        ('m3', 'gal'): lambda x: liters_to_gallons(cubic_meters_to_liters(x)),
    }

    conversion_function = conversions.get((from_unit, to_unit))
    if conversion_function:
        return conversion_function(value)

    raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")

if __name__ == '__main__':
    sample_liters = 1.0
    print(liters_to_milliliters(sample_liters))
    print(milliliters_to_liters(1000.0))
    print(cubic_meters_to_liters(1.0))
    print(liters_to_cubic_meters(1000.0))
    print(liters_to_gallons(sample_liters))
    print(gallons_to_liters(1.0))
    print(convert_volume(1.0, 'l', 'gal'))
    print(convert_volume(1.0, 'gal', 'l'))
    print(convert_volume(1.0, 'm3', 'l'))
    print(convert_volume(1000.0, 'l', 'm3'))
    print(convert_volume(1.0, 'l', 'ml'))
    print(convert_volume(1000.0, 'ml', 'l'))