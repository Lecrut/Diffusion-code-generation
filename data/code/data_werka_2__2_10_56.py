class VolumeConverter:
    LITERS_TO_MILLILITERS = 1000
    GALLONS_TO_MILLILITERS = 3785.41
    CUBIC_INCHES_TO_MILLILITERS = 16.3871

    def __init__(self):
        self.conversion_factors = {
            'liters': self.LITERS_TO_MILLILITERS,
            'gallons': self.GALLONS_TO_MILLILITERS,
            'cubic_inches': self.CUBIC_INCHES_TO_MILLILITERS
        }

    def convert_volume(self, volume):
        value = volume['value']
        unit = volume['unit'].lower()
        
        if value < 0:
            raise ValueError("Volume values cannot be negative.")
        if unit not in self.conversion_factors:
            raise ValueError(f"Unsupported unit: {unit}")
        
        return value * self.conversion_factors[unit]

    def convert_volumes(self, volumes):
        return [self.convert_volume(volume) for volume in volumes]

if __name__ == '__main__':
    sample_volumes = [
        {'value': 1.0, 'unit': 'liters'},
        {'value': 2.0, 'unit': 'gallons'},
        {'value': 3.0, 'unit': 'cubic_inches'}
    ]

    converter = VolumeConverter()
    converted_volumes = converter.convert_volumes(sample_volumes)
    print(converted_volumes)

    try:
        invalid_volume = {'value': -1.0, 'unit': 'liters'}
        converter.convert_volume(invalid_volume)
    except ValueError as e:
        print(e)

    try:
        unsupported_unit_volume = {'value': 1.0, 'unit': 'quarts'}
        converter.convert_volume(unsupported_unit_volume)
    except ValueError as e:
        print(e)