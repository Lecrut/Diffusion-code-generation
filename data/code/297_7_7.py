class VolumeConverter:
    def __init__(self):
        self.conversion_factor = 264.172

    def convert_cubic_meters_to_gallons(self, cubic_meters):
        return cubic_meters * self.conversion_factor

if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.convert_cubic_meters_to_gallons(1))
    print(converter.convert_cubic_meters_to_gallons(2))