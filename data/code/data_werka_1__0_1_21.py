class UnitConverter:
    METER_TO_FOOT = 3.28084
    METER_TO_KILOMETER = 0.001
    FOOT_TO_METER = 0.3048
    KILOMETER_TO_METER = 1000

    def convert(self, value, from_unit, to_unit):
        if from_unit == "meters" and to_unit == "feet":
            return value * self.METER_TO_FOOT
        elif from_unit == "meters" and to_unit == "kilometers":
            return value * self.METER_TO_KILOMETER
        elif from_unit == "feet" and to_unit == "meters":
            return value * self.FOOT_TO_METER
        elif from_unit == "feet" and to_unit == "kilometers":
            return value * self.FOOT_TO_METER * self.METER_TO_KILOMETER
        elif from_unit == "kilometers" and to_unit == "meters":
            return value * self.KILOMETER_TO_METER
        elif from_unit == "kilometers" and to_unit == "feet":
            return value * self.KILOMETER_TO_METER * self.METER_TO_FOOT
        elif from_unit == to_unit:
            return value
        else:
            raise ValueError("Unsupported conversion")

if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.convert(10, "meters", "feet"))
    print(converter.convert(5, "kilometers", "meters"))
    print(converter.convert(100, "feet", "kilometers"))