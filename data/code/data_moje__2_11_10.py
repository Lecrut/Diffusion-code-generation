def standardize_volume(measurements):
    conversion_factors = {
        'cubic_meter': 1.0,
        'liter': 0.001,
        'gallon': 0.00378541,
        'quart': 0.000946353,
        'pint': 0.000473176,
        'cup': 0.000236588,
        'fluid_ounce': 0.0000295735,
        'cubic_foot': 0.0283168,
        'cubic_inch': 0.0000163871,
        'cubic_yard': 0.764555
    }
    standardized = {}
    for material, value in measurements.items():
        if isinstance(value, tuple) and len(value) == 2:
            amount, unit = value
        else:
            amount = value
            unit = 'cubic_meter'
        unit_lower = unit.lower()
        if unit_lower not in conversion_factors:
            raise ValueError(f"Unknown unit: {unit}")
        cubic_meters = amount * conversion_factors[unit_lower]
        standardized[material] = cubic_meters
    return standardized

if __name__ == '__main__':
    sample_data = {
        'water': 10.0,
        'sand': ('5.5', 'liter'),
        'oil': ('2.0', 'gallon'),
        'gravel': ('1000', 'cubic_foot')
    }
    result = standardize_volume(sample_data)
    for key, value in result.items():
        print(f"{key}: {value}")