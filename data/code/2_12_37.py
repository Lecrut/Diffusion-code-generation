class VolumeConverter:
    FEET_PER_METER = 3.28084

    def __init__(self):
        self.conversion_factor = self.FEET_PER_METER ** 3

    def convert(self, meters):
        if meters < 0:
            raise ValueError("Volume cannot be negative")
        return meters * self.conversion_factor

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_values = [1.5, 7.2, 20.0, 0]
    for value in sample_values:
        try:
            result = converter.convert(value)
            print(f"{value} cubic meters is {result:.2f} cubic feet")
        except ValueError as e:
            print(e)