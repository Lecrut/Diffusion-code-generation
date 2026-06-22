class LengthConverter:
    def __init__(self):
        self.conversion_factor = 0.3048

    def convert_feet_to_meters(self, length_feet):
        return length_feet * self.conversion_factor

if __name__ == '__main__':
    converter = LengthConverter()
    result_10_ft = converter.convert_feet_to_meters(10.0)
    print(f"10.0 ft converted to meters: {result_10_ft}")
    result_5_5_ft = converter.convert_feet_to_meters(5.5)
    print(f"5.5 ft converted to meters: {result_5_5_ft}")