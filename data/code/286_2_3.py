class UnitConverter:
    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == "meters":
            if to_unit == "kilometers":
                return value / 1000.0
            elif to_unit == "miles":
                return value / 1609.34
            elif to_unit == "feet":
                return value * 3.28084
            elif to_unit == "inches":
                return value * 39.3701
        elif from_unit == "kilometers":
            if to_unit == "meters":
                return value * 1000.0
            elif to_unit == "miles":
                return value / 1.60934
            elif to_unit == "feet":
                return value * 1609.34
            elif to_unit == "inches":
                return value * 3937.01
        elif from_unit == "miles":
            if to_unit == "kilometers":
                return value * 1.60934
            elif to_unit == "meters":
                return value * 1609.34
            elif to_unit == "feet":
                return value * 5280.0
            elif to_unit == "inches":
                return value * 63360.0
        elif from_unit == "feet":
            if to_unit == "meters":
                return value * 0.3048
            elif to_unit == "kilometers":
                return value * 0.0003048
            elif to_unit == "miles":
                return value / 5280.0
            elif to_unit == "inches":
                return value * 12.0
        elif from_unit == "inches":
            if to_unit == "meters":
                return value / 39.3701
            elif to_unit == "feet":
                return value / 12.0
            elif to_unit == "miles":
                return value / 63360.0
            elif to_unit == "kilometers":
                return value / 160934.0
        else:
            raise ValueError("Unsupported unit")
if __name__ == '__main__':
    converter = UnitConverter()
    test_value = 10
    print(f"Converting {test_value} meters to kilometers: {converter.convert(test_value, 'meters', 'kilometers'):.4f}")
    print(f"Converting {test_value} kilometers to miles: {converter.convert(test_value, 'kilometers', 'miles'):.4f}")
    print(f"Converting {test_value} miles to feet: {converter.convert(test_value, 'miles', 'feet'):.4f}")
    print(f"Converting {test_value} feet to inches: {converter.convert(test_value, 'feet', 'inches'):.4f}")
    print(f"Converting {test_value} inches to meters: {converter.convert(test_value, 'inches', 'meters'):.4f}")
    print(f"Converting 50 kilometers to meters: {converter.convert(50, 'kilometers', 'meters'):.4f}")
    print(f"Converting 10000 feet to miles: {converter.convert(10000, 'feet', 'miles'):.4f}")