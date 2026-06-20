class VolumeConverter:

    def __init__(self):
        self.conversion_factors = {'L_to_ml': 1000, 'ml_to_L': 0.001, 'm3_to_in3': 61023.7441, 'in3_to_m3': 1 / 61023.7441}

    def liters_to_milliliters(self, liters):
        if liters < 0:
            raise ValueError('Volume cannot be negative')
        return liters * self.conversion_factors['L_to_ml']

    def milliliters_to_liters(self, milliliters):
        if milliliters < 0:
            raise ValueError('Volume cannot be negative')
        return milliliters * self.conversion_factors['ml_to_L']

    def cubic_meters_to_cubic_inches(self, cubic_meters):
        if cubic_meters < 0:
            raise ValueError('Volume cannot be negative')
        return cubic_meters * self.conversion_factors['m3_to_in3']

    def cubic_inches_to_cubic_meters(self, cubic_inches):
        if cubic_inches < 0:
            raise ValueError('Volume cannot be negative')
        return cubic_inches * self.conversion_factors['in3_to_m3']
if __name__ == '__main__':
    converter = VolumeConverter()
    liters_value = 2.5
    ml_value = 500
    m3_value = 1.0
    in3_value = 1000
    print(f'Liters to Milliliters: {converter.liters_to_milliliters(liters_value)}')
    print(f'Milliliters to Liters: {converter.milliliters_to_liters(ml_value)}')
    print(f'Cubic Meters to Cubic Inches: {converter.cubic_meters_to_cubic_inches(m3_value)}')
    print(f'Cubic Inches to Cubic Meters: {converter.cubic_inches_to_cubic_meters(in3_value)}')