class Volume:
    UNIT_CONVERSIONS = {
        'liters': 1e-3,
        'milliliters': 1e3,
        'gallons': 2.64172052 * 1e-6,
        'cubic_meters': 1e-6
    }

    def __init__(self, cubic_centimeters):
        if cubic_centimeters < 0:
            raise ValueError("Volume cannot be negative")
        self.cubic_centimeters = cubic_centimeters

    def convert_to(self, unit):
        if unit not in self.UNIT_CONVERSIONS:
            raise ValueError(f"Unsupported unit: {unit}")
        return self.cubic_centimeters * self.UNIT_CONVERSIONS[unit]

if __name__ == '__main__':
    sample_volume = Volume(500)
    print('Liters:', sample_volume.convert_to('liters'))
    print('Milliliters:', sample_volume.convert_to('milliliters'))
    print('Gallons:', sample_volume.convert_to('gallons'))
    print('Cubic Meters:', sample_volume.convert_to('cubic_meters'))