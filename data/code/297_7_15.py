class VolumeConverter:
    def __init__(self):
        self.conversion_factor = 264.172

    def cubic_meters_to_gallons(self, cubic_meters):
        if not isinstance(cubic_meters, (int, float)) or cubic_meters < 0:
            raise ValueError("Invalid input. Please provide a non-negative number in cubic meters.")
        return cubic_meters * self.conversion_factor

if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.cubic_meters_to_gallons(1))
    print(converter.cubic_meters_to_gallons(2))