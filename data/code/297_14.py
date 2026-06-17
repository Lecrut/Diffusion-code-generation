from abc import ABC, abstractmethod
class Unit(ABC):
    @abstractmethod
    def to_base(self, value):
        pass
    @abstractmethod
    def from_base(self, base_value):
        pass
    @abstractmethod
    def convert(self, value, target_unit):
        pass
class Length(Unit):
    def __init__(self, value):
        self._value = value
    def to_base(self, value):
        return value
    def from_base(self, base_value):
        return base_value
    def convert(self, value, target_unit):
        if isinstance(target_unit, Length):
            return value
        raise TypeError("Cannot convert length to non-length unit")
class Mass(Unit):
    def __init__(self, value):
        self._value = value
    def to_base(self, value):
        return value
    def from_base(self, base_value):
        return base_value
    def convert(self, value, target_unit):
        if isinstance(target_unit, Mass):
            return value
        raise TypeError("Cannot convert mass to non-mass unit")
class Temperature(Unit):
    def __init__(self, value):
        self._value = value
    def to_base(self, value):
        return value
    def from_base(self, base_value):
        return base_value
    def convert(self, value, target_unit):
        if isinstance(target_unit, Temperature):
            return value
        raise TypeError("Cannot convert temperature to non-temperature unit")
class ConversionManager:
    def __init__(self):
        self.units = {
            "meter": Length(1.0),
            "kilometer": Length(1000.0),
            "gram": Mass(1.0),
            "kilogram": Mass(1000.0),
            "celsius": Temperature(0.0),
            "fahrenheit": Temperature(32.0)
        }
    def get_unit(self, unit_name):
        if unit_name not in self.units:
            raise ValueError(f"Unknown unit: {unit_name}")
        return self.units[unit_name]
    def convert_value(self, value, from_unit, to_unit):
        if from_unit not in self.units or to_unit not in self.units:
            raise ValueError("One or both units are unknown.")
        from_obj = self.units[from_unit]
        to_obj = self.units[to_unit]
        base_value = from_obj.to_base(value)
        result = to_obj.from_base(base_value)
        return result
if __name__ == '__main__':
    manager = ConversionManager()
    print("--- Length Conversion (Meter to Kilometer) ---")
    try:
        length_val = 500.0
        from_unit = "meter"
        to_unit = "kilometer"
        result = manager.convert_value(length_val, from_unit, to_unit)
        print(f"{length_val} {from_unit} is equal to {result} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Mass Conversion (Gram to Kilogram) ---")
    try:
        mass_val = 2500.0
        from_unit = "gram"
        to_unit = "kilogram"
        result = manager.convert_value(mass_val, from_unit, to_unit)
        print(f"{mass_val} {from_unit} is equal to {result} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Temperature Conversion (Celsius to Fahrenheit) ---")
    try:
        temp_val = 20.0
        from_unit = "celsius"
        to_unit = "fahrenheit"
        result = manager.convert_value(temp_val, from_unit, to_unit)
        print(f"{temp_val} {from_unit} is equal to {result} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Invalid Conversion Test ---")
    try:
        manager.convert_value(10, "meter", "gram")
    except ValueError as e:
        print(f"Caught expected error: {e}")