def convert_volumes_to_milliliters(volumes):
    LITERS_TO_MILLILITERS = 1000
    GALLONS_TO_MILLILITERS = 3785.41
    CUBIC_INCHES_TO_MILLILITERS = 16.3871

    def convert_single_volume(volume):
        value, unit = volume['value'], volume['unit'].lower()
        if value < 0:
            raise ValueError("Volume values cannot be negative.")
        if unit == 'liters':
            return value * LITERS_TO_MILLILITERS
        elif unit == 'gallons':
            return value * GALLONS_TO_MILLILITERS
        elif unit == 'cubic_inches':
            return value * CUBIC_INCHES_TO_MILLILITERS
        else:
            raise ValueError(f"Unsupported unit: {unit}")

    converted_volumes = [convert_single_volume(volume) for volume in volumes]
    return converted_volumes

if __name__ == '__main__':
    sample_volumes = [
        {'value': 2.5, 'unit': 'liters'},
        {'value': 10, 'unit': 'gallons'},
        {'value': 100, 'unit': 'cubic inches'}
    ]
    converted_results = convert_volumes_to_milliliters(sample_volumes)
    print(converted_results)