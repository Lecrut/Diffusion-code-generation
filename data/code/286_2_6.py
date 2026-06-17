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
    print("--- Test Case 1: Meters to Kilometers ---")
    meters = 1000
    result1 = converter.convert(meters, "meters", "kilometers")
    print(f"{meters} meters is {result1} kilometers")
    print("\n--- Test Case 2: Miles to Feet ---")
    miles = 1
    result2 = converter.convert(miles, "miles", "feet")
    print(f"{miles} miles is {result2} feet")
    print("\n--- Test Case 3: Feet to Inches ---")
    feet = 5
    result3 = converter.convert(feet, "feet", "inches")
    print(f"{feet} feet is {result3} inches")
    print("\n--- Test Case 4: Inches to Meters ---")
    inches = 39.3701
    result4 = converter.convert(inches, "inches", "meters")
    print(f"{inches} inches is {result4} meters")
    print("\n--- Test Case 5: Kilometers to Miles ---")
    km = 10
    result5 = converter.convert(km, "kilometers", "miles")
    print(f"{km} kilometers is {result5} miles")