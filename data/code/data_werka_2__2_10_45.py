class VolumeConverter:
    LITERS_TO_MILLILITERS = 1000
    GALLONS_TO_MILLILITERS = 3785.41
    CUBIC_INCHES_TO_MILLILITERS = 16.3871

    def __init__(self):
        self.conversion_factors = {'liters': self.LITERS_TO_MILLILITERS, 'gallons': self.GALLONS_TO_MILLILITERS, 'cubic_inches': self.CUBIC_INCHES_TO_MILLILITERS}

    def convert_volume(self, volume):
        value = volume['value']
        unit = volume['unit'].lower()
        if value < 0:
            raise ValueError('Volume values cannot be negative.')
        if unit not in self.conversion_factors:
            raise ValueError(f'Unsupported unit: {unit}')
        return value * self.conversion_factors[unit]

    def convert_volumes(self, volumes):
        return [self.convert_volume(volume) for volume in volumes]
if __name__ == '__main__':
    sample_volumes = [{'value': 2.0, 'unit': 'liters'}, {'value': 1.0, 'unit': 'gallons'}, {'value': 61.0237, 'unit': 'cubic inches'}, {'value': -1.0, 'unit': 'liters'}, {'value': 0.0, 'unit': 'liters'}]
    converter = VolumeConverter()
    try:
        converted_volumes = converter.convert_volumes(sample_volumes)
        for original, converted in zip(sample_volumes, converted_volumes):
            print(f"Original: {original['value']} {original['unit']}, Converted: {converted} ml")
    except ValueError as e:
        print(e)