def convert_volumes_to_milliliters(volumes):
    LITERS_TO_MILLILITERS = 1000
    GALLONS_TO_MILLILITERS = 3785.41
    CUBIC_INCHES_TO_MILLILITERS = 16.3871

    conversion_factors = {
        'liters': LITERS_TO_MILLILITERS,
        'gallons': GALLONS_TO_MILLILITERS,
        'cubic_inches': CUBIC_INCHES_TO_MILLILITERS
    }

    def convert_single_volume(volume):
        value, unit = volume['value'], volume['unit'].lower()
        if value < 0:
            raise ValueError("Volume values cannot be negative.")
        if unit not in conversion_factors:
            raise ValueError(f"Unsupported unit: {unit}")
        return value * conversion_factors[unit]

    converted_volumes = [convert_single_volume(volume) for volume in volumes]
    return converted_volumes

if __name__ == '__main__':
    sample_volumes = [
        {'value': 2, 'unit': 'liters'},
        {'value': 1, 'unit': 'gallons'},
        {'value': 1000, 'unit': 'cubic inches'}
    ]
    try:
        print(convert_volumes_to_milliliters(sample_volumes))
    except ValueError as e:
        print(e)