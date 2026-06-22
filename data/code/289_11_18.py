class DistanceConverter:
    def convert_to_feet(self, meters):
        return [round(meter * 3.28084, 2) for meter in meters]

if __name__ == '__main__':
    converter = DistanceConverter()
    sample_meters = [1.5, 2.5, 3.5]
    feet_values = converter.convert_to_feet(sample_meters)
    print(feet_values)