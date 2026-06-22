def convert_volumes_to_milliliters(volumes):
    conversion_factors = {'liters': 1000, 'gallons': 3785.41, 'cubic_inches': 16.3871}

    def validate_and_convert(volume):
        value, unit = (volume['value'], volume['unit'].lower())
        if value < 0:
            raise ValueError('Volume values cannot be negative.')
        if unit not in conversion_factors:
            raise ValueError(f'Unsupported unit: {unit}')
        return value * conversion_factors[unit]
    converted_volumes = [validate_and_convert(volume) for volume in volumes]
    return converted_volumes
if __name__ == '__main__':
    sample_volumes = [{'value': 1, 'unit': 'liters'}, {'value': 2, 'unit': 'gallons'}, {'value': 3, 'unit': 'cubic_inches'}, {'value': -1, 'unit': 'liters'}, {'value': 0, 'unit': 'liters'}]
    try:
        print(convert_volumes_to_milliliters(sample_volumes))
    except ValueError as e:
        print(e)