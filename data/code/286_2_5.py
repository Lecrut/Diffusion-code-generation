class UnitConverter:
    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == "meters":
            if to_unit == "kilometers":
                return value / 1000
            elif to_unit == "miles":
                return value * 0.000621371
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
                return value * 3280.84
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
                return value * 12
        elif from_unit == "inches":
            if to_unit == "meters":
                return value / 39.3701
            elif to_unit == "feet":
                return value / 12
            elif to_unit == "miles":
                return value / 63360.0
            elif to_unit == "kilometers":
                return value * 0.0000254801
        else:
            raise ValueError("Unsupported starting unit")
if __name__ == '__main__':
    converter = UnitConverter()
    test_cases = [
        (10, "meters", "kilometers"),
        (1, "miles", "feet"),
        (500, "meters", "feet"),
        (100, "inches", "meters"),
        (1, "kilometers", "miles"),
        (10, "feet", "inches"),
        (2.5, "miles", "meters")
    ]
    for value, from_unit, to_unit in test_cases:
        try:
            result = converter.convert(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")
        except ValueError as e:
            print(f"Error for {value} {from_unit} to {to_unit}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for {value} {from_unit} to {to_unit}: {e}")