def convert_volumes_to_milliliters(volumes):
    conversion_factors = {'liters': 1000, 'gallons': 3785.41, 'cubic_inches': 16.3871}
    converted_volumes = []
    for volume in volumes:
        value, unit = volume
        if value < 0:
            raise ValueError('Volume values cannot be negative')
        converted_volume = value * conversion_factors.get(unit.lower(), 0)
        converted_volumes.append(converted_volume)
    return converted_volumes
if __name__ == '__main__':
    sample_volumes = [(2, 'liters'), (1, 'gallons'), (100, 'cubic_inches'), (0, 'liters'), (-1, 'liters')]
    try:
        converted = convert_volumes_to_milliliters(sample_volumes)
        print(converted)
    except ValueError as e:
        print(e)