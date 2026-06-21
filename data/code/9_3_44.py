class VolumeConverter:
    def __init__(self):
        self.conversion_factors = {
            'ml': 0.001,
            'cl': 0.01,
            'dl': 0.1,
            'l': 1.0,
            'fl oz': 0.0295735296,
            'cup': 0.2365882365,
            'pt': 0.473176473,
            'qt': 0.946352946,
            'gal': 3.785411784
        }

    def convert_to_liters(self, volume, unit):
        if unit.lower() not in self.conversion_factors:
            raise ValueError(f"Unsupported unit: {unit}")
        return volume * self.conversion_factors[unit.lower()]

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_values = [
        (100, 'ml'),
        (250, 'cl'),
        (1, 'dl'),
        (5, 'l'),
        (8, 'fl oz'),
        (2, 'cup'),
        (1, 'pt'),
        (1, 'qt'),
        (1, 'gal')
    ]
    for volume, unit in sample_values:
        print(f"{volume} {unit} is {converter.convert_to_liters(volume, unit)} liters")