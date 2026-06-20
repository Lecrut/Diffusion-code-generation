class DistanceConverter:
    MILES_TO_KM = 1.60934
    MILES_TO_M = 1609.34
    KM_TO_MILES = 0.621371
    KM_TO_M = 1000.0
    M_TO_MILES = 0.000621371
    M_TO_KM = 0.001

    def __init__(self):
        self.units = {
            "miles": "miles",
            "kilometers": "kilometers",
            "meters": "meters"
        }

    def convert(self, value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if from_unit not in self.units:
            raise ValueError(f"Unsupported unit: {from_unit}")
        if to_unit not in self.units:
            raise ValueError(f"Unsupported unit: {to_unit}")

        if from_unit == to_unit:
            return value

        if from_unit == "miles":
            if to_unit == "kilometers":
                return value * self.MILES_TO_KM
            elif to_unit == "meters":
                return value * self.MILES_TO_M
        elif from_unit == "kilometers":
            if to_unit == "miles":
                return value * self.KM_TO_MILES
            elif to_unit == "meters":
                return value * self.KM_TO_M
        elif from_unit == "meters":
            if to_unit == "miles":
                return value * self.M_TO_MILES
            elif to_unit == "kilometers":
                return value * self.M_TO_KM

        raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported")

if __name__ == "__main__":
    converter = DistanceConverter()

    miles = 10
    km = converter.convert(miles, "miles", "kilometers")
    print(km)

    meters = 1000
    miles_from_m = converter.convert(meters, "meters", "miles")
    print(miles_from_m)

    km_to_m = converter.convert(5, "kilometers", "meters")
    print(km_to_m)