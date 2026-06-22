class DistanceConverter:
    CONVERSION_FACTOR = 3.28084

    @staticmethod
    def meters_to_feet(meters):
        return [round(meter * DistanceConverter.CONVERSION_FACTOR, 2) for meter in meters]

if __name__ == '__main__':
    sample_meters = [10.0, 20.0, 30.0]
    converted_feet = DistanceConverter.meters_to_feet(sample_meters)
    print(converted_feet)