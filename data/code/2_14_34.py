class VolumeConverter:
    def __init__(self):
        self.conversion_factor = 0.0610237440947

    def convert_to_cubic_inches(self, cubic_centimeters):
        return cubic_centimeters * self.conversion_factor

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_values = [300, 800, 1200]
    for value in sample_values:
        result = converter.convert_to_cubic_inches(value)
        print(f'{value} cubic centimeters is {result:.6f} cubic inches')