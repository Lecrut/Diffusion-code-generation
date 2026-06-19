def convert_volumes_to_milliliters(volumes):
    conversion_factors = {'liters': 1000, 'gallons': 3785.41, 'cubic_inches': 16.3871}
    converted_volumes = []
    for volume in volumes:
        value, unit = (volume['value'], volume['unit'].lower())
        if value <= 0:
            converted_volumes.append(0)
        elif unit in conversion_factors:
            converted_volumes.append(value * conversion_factors[unit])
        else:
            converted_volumes.append(None)
    return converted_volumes
if __name__ == '__main__':
    sample_volumes = [{'value': 2, 'unit': 'liters'}, {'value': 5, 'unit': 'gallons'}, {'value': 100, 'unit': 'cubic inches'}, {'value': -3, 'unit': 'liters'}, {'value': 0, 'unit': 'gallons'}, {'value': 42, 'unit': 'unknown'}]
    converted = convert_volumes_to_milliliters(sample_volumes)
    print(converted)