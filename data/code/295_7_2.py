class UnitConverter:
    def __init__(self, conversion_factors):
        self.conversion_factors = conversion_factors
    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors:
            raise ValueError("One or both units are not defined in the conversion factors.")
        if from_unit == to_unit:
            return value
        if (from_unit, to_unit) in self.conversion_factors:
            return value * self.conversion_factors[(from_unit, to_unit)]
        if (to_unit, from_unit) in self.conversion_factors:
            return value / self.conversion_factors[(to_unit, from_unit)]
        raise ValueError(f"Conversion factor not found between {from_unit} and {to_unit}")
if __name__ == '__main__':
    conversion_data = {
        ('meter', 'kilometer'): 1000.0,
        ('centimeter', 'meter'): 0.01,
        ('pound', 'kilogram'): 0.453592,
        ('meter', 'centimeter'): 100.0
    }
    converter = UnitConverter(conversion_data)
    print("--- Unit Conversion Tests ---")
    try:
        result1 = converter.convert(5, 'meter', 'kilometer')
        print(f"5 meters is {result1} kilometers")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result2 = converter.convert(300, 'centimeter', 'meter')
        print(f"300 centimeters is {result2} meters")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result3 = converter.convert(10, 'pound', 'kilogram')
        print(f"10 pounds is {result3} kilograms")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result4 = converter.convert(2, 'meter', 'centimeter')
        print(f"2 meters is {result4} centimeters")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result5 = converter.convert(10, 'meter', 'meter')
        print(f"10 meters is {result5} meters")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        converter.convert(1, 'meter', 'furlong')
    except ValueError as e:
        print(f"Successfully caught expected error for unknown unit: {e}")