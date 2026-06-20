class DistanceConverter:
    MILES_TO_KILOMETERS = 1.60934
    KILOMETERS_TO_MILES = 1 / MILES_TO_KILOMETERS
    MILES_TO_METERS = MILES_TO_KILOMETERS * 1000
    KILOMETERS_TO_METERS = 1000
    METERS_TO_KILOMETERS = 1 / KILOMETERS_TO_METERS
    METERS_TO_MILES = 1 / MILES_TO_METERS
    METERS_TO_KILOMETERS = 1 / KILOMETERS_TO_METERS

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        
        lower_from = from_unit.lower()
        lower_to = to_unit.lower()

        if lower_from == "miles":
            if lower_to == "kilometers":
                return value * self.MILES_TO_KILOMETERS
            elif lower_to == "meters":
                return value * self.MILES_TO_METERS
        elif lower_from == "kilometers":
            if lower_to == "miles":
                return value * self.KILOMETERS_TO_MILES
            elif lower_to == "meters":
                return value * self.KILOMETERS_TO_METERS
        elif lower_from == "meters":
            if lower_to == "miles":
                return value * self.METERS_TO_MILES
            elif lower_to == "kilometers":
                return value * self.METERS_TO_KILOMETERS
        
        raise ValueError(f"Unsupported unit conversion from {from_unit} to {to_unit}")

if __name__ == '__main__':
    converter = DistanceConverter()
    result = converter.convert(5, "miles", "kilometers")
    print(result)