def validate_volume(volume):
    if volume['value'] < 0:
        raise ValueError("Volume values cannot be negative.")
    if volume['unit'].lower() not in ['liters', 'gallons', 'cubic_inches']:
        raise ValueError(f"Unsupported unit: {volume['unit']}")

def convert_single_volume_to_milliliters(volume):
    value = volume['value']
    unit = volume['unit'].lower()
    if unit == 'liters':
        return value * 1000
    elif unit == 'gallons':
        return value * 3785.41
    elif unit == 'cubic_inches':
        return value * 16.3871

def convert_volumes_to_milliliters(volumes):
    converted_volumes = []
    for volume in volumes:
        validate_volume(volume)
        converted_value = convert_single_volume_to_milliliters(volume)
        converted_volumes.append(converted_value)
    return converted_volumes

if __name__ == '__main__':
    sample_volumes = [
        {'value': 1, 'unit': 'liters'},
        {'value': 2, 'unit': 'gallons'},
        {'value': 3, 'unit': 'cubic_inches'}
    ]
    print(convert_volumes_to_milliliters(sample_volumes))