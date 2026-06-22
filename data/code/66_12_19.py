class UnitConverter:
    METERS_PER_KILOMETER: int = 1000

    @staticmethod
    def convert_kilometers_to_meters(km: int) -> int:
        if not isinstance(km, int):
            raise TypeError("Input must be an integer")
        return km * UnitConverter.METERS_PER_KILOMETER

if __name__ == '__main__':
    test_values = [0, 1, 42, 100, 999]
    for val in test_values:
        converted = UnitConverter.convert_kilometers_to_meters(val)
        print(converted)