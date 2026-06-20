class DistanceConverter:
    MILES_TO_KM = 1.60934
    MILES_TO_M = 1609.34
    KM_TO_M = 1000.0

    @staticmethod
    def convert(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value

        if from_unit == "miles":
            if to_unit == "kilometers":
                return value * DistanceConverter.MILES_TO_KM
            elif to_unit == "meters":
                return value * DistanceConverter.MILES_TO_M
        elif from_unit == "kilometers":
            if to_unit == "miles":
                return value / DistanceConverter.MILES_TO_KM
            elif to_unit == "meters":
                return value * DistanceConverter.KM_TO_M
        elif from_unit == "meters":
            if to_unit == "miles":
                return value / DistanceConverter.MILES_TO_M
            elif to_unit == "kilometers":
                return value / DistanceConverter.KM_TO_M

        raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(1, "miles", "kilometers"))
    print(converter.convert(1, "kilometers", "meters"))
    print(converter.convert(1609.34, "meters", "miles"))