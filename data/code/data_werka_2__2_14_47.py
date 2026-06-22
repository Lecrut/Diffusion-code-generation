class VolumeConverter:
    def __init__(self):
        self.conversion_factor = 0.0610237440947

    def cubic_centimeters_to_cubic_inches(self, cc):
        if not isinstance(cc, (int, float)):
            raise ValueError("Input must be a number")
        if cc < 0:
            raise ValueError("Volume cannot be negative")
        return cc * self.conversion_factor

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_values = [150, 400, 800]
    for value in sample_values:
        try:
            result = converter.cubic_centimeters_to_cubic_inches(value)
            print(f'{value} cubic centimeters is {result:.6f} cubic inches')
        except ValueError as e:
            print(e)