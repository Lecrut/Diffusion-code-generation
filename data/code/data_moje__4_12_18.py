class DistanceConverter:
    MILES_TO_KM = 1.60934
    MILES_TO_M = 1609.34
    KM_TO_MILES = 1 / 1.60934
    KM_TO_M = 1000
    M_TO_MILES = 1 / 1609.34
    M_TO_KM = 0.001

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        
        if from_unit == "miles" and to_unit == "kilometers":
            return value * self.MILES_TO_KM
        elif from_unit == "kilometers" and to_unit == "miles":
            return value * self.KM_TO_MILES
        elif from_unit == "miles" and to_unit == "meters":
            return value * self.MILES_TO_M
        elif from_unit == "meters" and to_unit == "miles":
            return value * self.M_TO_MILES
        elif from_unit == "kilometers" and to_unit == "meters":
            return value * self.KM_TO_M
        elif from_unit == "meters" and to_unit == "kilometers":
            return value * self.M_TO_KM
        else:
            raise ValueError(f"Unsupported unit conversion: {from_unit} to {to_unit}")

if __name__ == '__main__':
    converter = DistanceConverter()
    result = converter.convert(5, "miles", "kilometers")
    print(result)