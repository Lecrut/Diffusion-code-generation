def convert_to_milliliters(volumes):
    conversion_factors = {'liters': 1000, 'gallons': 3785.41, 'cubic_inches': 16.3871}
    converted_volumes = []
    for volume, unit in volumes:
        if volume < 0:
            raise ValueError('Volume cannot be negative')
        converted_volume = volume * conversion_factors.get(unit.lower(), 0)
        converted_volumes.append(converted_volume)
    return converted_volumes
if __name__ == '__main__':
    sample_volumes = [(1, 'liters'), (2, 'gallons'), (3, 'cubic_inches'), (0, 'liters'), (-1, 'liters')]
    try:
        converted = convert_to_milliliters(sample_volumes)
        print(converted)
    except ValueError as e:
        print(e)