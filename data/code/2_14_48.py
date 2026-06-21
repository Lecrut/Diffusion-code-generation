class VolumeConverter:
    def __init__(self):
        self.conversion_factor = 0.0610237440947

    def cubic_centimeters_to_cubic_inches(self, cc):
        return cc * self.conversion_factor

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_values = [50, 200, 800]
    for value in sample_values:
        result = converter.cubic_centimeters_to_cubic_inches(value)
        print(f'{value} cubic centimeters is {result:.6f} cubic inches')