class UnitConverter:
    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == "meters":
            if to_unit == "kilometers":
                return value / 1000
            elif to_unit == "miles":
                return value / 1609.34
            elif to_unit == "feet":
                return value * 3.28084
            elif to_unit == "inches":
                return value * 39.3701
        elif from_unit == "kilometers":
            if to_unit == "meters":
                return value * 1000
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
                return value * 5280
            elif to_unit == "inches":
                return value * 63360
        elif from_unit == "feet":
            if to_unit == "meters":
                return value / 3.28084
            elif to_unit == "kilometers":
                return value / 1609.34
            elif to_unit == "miles":
                return value / 5280
            elif to_unit == "inches":
                return value * 12
        elif from_unit == "inches":
            if to_unit == "meters":
                return value / 39.3701
            elif to_unit == "feet":
                return value / 12
            elif to_unit == "miles":
                return value / 63360
            elif to_unit == "kilometers":
                return value / 160934
        else:
            raise ValueError("Unsupported unit")
if __name__ == '__main__':
    converter = UnitConverter()
    test_cases = [
        (10, "meters", "kilometers"),
        (1, "miles", "feet"),
        (50, "feet", "inches"),
        (2, "kilometers", "meters"),
        (100, "miles", "meters"),
        (12, "inches", "feet"),
        (5, "meters", "meters")
    ]
    for value, from_u, to_u in test_cases:
        try:
            result = converter.convert(value, from_u, to_u)
            print(f"{value} {from_u} is equal to {result:.4f} {to_u}")
        except ValueError as e:
            print(f"Error for conversion: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")