class LengthUnitConverter:
    METERS_TO_FEET_RATIO = 3.28084

    @staticmethod
    def convert_meters_to_feet(meters):
        if not isinstance(meters, (int, float)):
            raise ValueError("Input must be a numeric value.")
        return meters * LengthUnitConverter.METERS_TO_FEET_RATIO

if __name__ == '__main__':
    sample_value = 10
    result = LengthUnitConverter.convert_meters_to_feet(sample_value)
    print(result)