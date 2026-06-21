def convert_volume(value, source_unit, target_unit='liters'):
    conversion_rates = {
        'liters': 1.0,
        'milliliters': 0.001,
        'cubic_meters': 1000.0,
        'gallons': 3.78541,
        'quarts': 0.946353,
        'pints': 0.473176,
        'cups': 0.24,
        'fluid_ounces': 0.0295735,
        'tablespoons': 0.0147868,
        'teaspoons': 0.00492892,
        'cubic_inches': 0.0163871,
        'cubic_feet': 28.3168,
        'cubic_yards': 764.555,
        'barrels': 158.987,
        'deciliters': 0.1,
        'centiliters': 0.01,
        'microliters': 1e-6,
        'nanoliters': 1e-9,
        'picoliters': 1e-12
    }

    source_unit = source_unit.lower()
    target_unit = target_unit.lower()

    if value < 0:
        raise ValueError("Volume cannot be negative")

    if source_unit not in conversion_rates:
        raise ValueError(f"Unknown source unit: {source_unit}")

    if target_unit not in conversion_rates:
        raise ValueError(f"Unknown target unit: {target_unit}")

    liters = value * conversion_rates[source_unit]
    result = liters / conversion_rates[target_unit]

    return result

if __name__ == '__main__':
    print(convert_volume(1, 'gallons', 'liters'))
    print(convert_volume(500, 'milliliters', 'cups'))
    print(convert_volume(2, 'cubic_feet', 'liters'))
    print(convert_volume(10, 'liters', 'gallons'))
    print(convert_volume(1, 'barrels', 'gallons'))