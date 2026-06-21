class VolumeUnitConverter:
    LITERS_TO_GALLONS = 0.264172

    def convert(self, liters):
        if not isinstance(liters, (int, float)):
            raise ValueError("Input volume must be a number")
        return liters * self.LITERS_TO_GALLONS

if __name__ == '__main__':
    converter = VolumeUnitConverter()
    sample_values = [3.5, 8.0, 12.0, 24.0]
    for value in sample_values:
        print(f"{value} liters is {converter.convert(value)} gallons")