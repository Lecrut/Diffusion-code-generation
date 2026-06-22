class LengthConverter:
    FEET_TO_METERS = 0.3048

    @staticmethod
    def convert_feet_to_meters(feet):
        return feet * LengthConverter.FEET_TO_METERS

if __name__ == '__main__':
    length_feet = 10.0
    result_meters = LengthConverter.convert_feet_to_meters(length_feet)
    print(f"10.0 ft converted to meters: {result_meters}")