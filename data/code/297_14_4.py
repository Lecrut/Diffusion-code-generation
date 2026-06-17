from abc import ABC, abstractmethod
class UnitConverter(ABC):
    @abstractmethod
    def convert(self, value, from_unit, to_unit):
        pass
class LengthConverter(UnitConverter):
    def convert(self, value, from_unit, to_unit):
        if from_unit == "m" and to_unit == "cm":
            return value * 100
        elif from_unit == "cm" and to_unit == "m":
            return value / 100
        elif from_unit == "km" and to_unit == "m":
            return value * 1000
        elif from_unit == "m" and to_unit == "km":
            return value / 1000
        else:
            raise ValueError("Unsupported length conversion")
class TemperatureConverter(UnitConverter):
    def convert(self, value, from_unit, to_unit):
        if from_unit == "C" and to_unit == "F":
            return (value * 9/5) + 32
        elif from_unit == "F" and to_unit == "C":
            return (value - 32) * 5/9
        elif from_unit == "C" and to_unit == "K":
            return value + 273.15
        elif from_unit == "K" and to_unit == "C":
            return value - 273.15
        else:
            raise ValueError("Unsupported temperature conversion")
class AreaConverter(UnitConverter):
    def convert(self, value, from_unit, to_unit):
        if from_unit == "m2" and to_unit == "cm2":
            return value * 10000
        elif from_unit == "cm2" and to_unit == "m2":
            return value / 10000
        else:
            raise ValueError("Unsupported area conversion")
class UnitManager:
    def __init__(self):
        self.converters = {
            "length": {
                "m": LengthConverter(),
                "cm": LengthConverter()
            },
            "temperature": {
                "C": TemperatureConverter(),
                "F": TemperatureConverter(),
                "K": TemperatureConverter()
            },
            "area": {
                "m2": AreaConverter()
            }
        }
    def convert_value(self, category, value, from_unit, to_unit):
        if category == "length":
            converter = self.converters["length"].get(from_unit)
            if converter:
                return converter.convert(value, from_unit, to_unit)
        elif category == "temperature":
            converter = self.converters["temperature"].get(from_unit)
            if converter:
                return converter.convert(value, from_unit, to_unit)
        elif category == "area":
            converter = self.converters["area"].get(from_unit)
            if converter:
                return converter.convert(value, from_unit, to_unit)
        else:
            raise ValueError("Invalid category")
if __name__ == '__main__':
    manager = UnitManager()
    print("--- Length Conversion (m to cm) ---")
    try:
        result_len = manager.convert_value("length", 5, "m", "cm")
        print(f"5 m is {result_len} cm")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Length Conversion (km to m) ---")
    try:
        result_len2 = manager.convert_value("length", 2.5, "km", "m")
        print(f"2.5 km is {result_len2} m")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Temperature Conversion (C to F) ---")
    try:
        result_temp = manager.convert_value("temperature", 25, "C", "F")
        print(f"25 C is {result_temp} F")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Temperature Conversion (K to C) ---")
    try:
        result_temp2 = manager.convert_value("temperature", 300, "K", "C")
        print(f"300 K is {result_temp2} C")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Area Conversion (m2 to cm2) ---")
    try:
        result_area = manager.convert_value("area", 1, "m2", "cm2")
        print(f"1 m^2 is {result_area} cm^2")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Unsupported Conversion Example ---")
    try:
        manager.convert_value("length", 1, "m", "inch")
    except ValueError as e:
        print(f"Caught expected error: {e}")