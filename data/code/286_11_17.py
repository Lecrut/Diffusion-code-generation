class LengthConverter:
    METERS_TO_FEET = 1 / 0.3048

    @staticmethod
    def feet_to_meters(feet):
        return feet * LengthConverter.METERS_TO_FEET

if __name__ == '__main__':
    length_feet = 10.0
    result_meters = LengthConverter.feet_to_meters(length_feet)
    print(f"10.0 ft converted to meters: {result_meters}")