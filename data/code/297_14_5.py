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
            "meter": Length(1),
            "kilometer": Length(1000),
            "gram": Mass(1),
            "kilogram": Mass(1000),
            "celsius": Temperature(0),
            "fahrenheit": Temperature(32)
        }
    def get_unit(self, unit_name):
        if unit_name not in self.units:
            raise ValueError(f"Unknown unit: {unit_name}")
        return self.units[unit_name]
    def convert_value(self, value, from_unit, to_unit):
        from_obj = self.get_unit(from_unit)
        to_obj = self.get_unit(to_unit)
        if type(from_obj) is not type(to_obj):
            raise TypeError("Cannot convert between different types of units")
        base_value = from_obj.to_base(value)
        result = to_obj.from_base(base_value)
        return result
if __name__ == '__main__':
    manager = ConversionManager()
    print("--- Length Conversion ---")
    try:
        length_m = manager.get_unit("meter")
        length_km = manager.get_unit("kilometer")
        value_m = 500
        result_km = manager.convert_value(value_m, "meter", "kilometer")
        print(f"{value_m} meters is {result_km} kilometers")
        length_km_to_m = manager.convert_value(1500, "kilometer", "meter")
        print(f"1500 kilometers is {length_km_to_m} meters")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
    print("\n--- Mass Conversion ---")
    try:
        mass_kg = manager.get_unit("kilogram")
        mass_g = manager.get_unit("gram")
        value_kg = 2.5
        result_g = manager.convert_value(value_kg, "kilogram", "gram")
        print(f"{value_kg} kilograms is {result_g} grams")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
    print("\n--- Temperature Conversion ---")
    try:
        temp_c = manager.get_unit("celsius")
        temp_f = manager.get_unit("fahrenheit")
        value_c = 25
        result_f = manager.convert_value(value_c, "celsius", "fahrenheit")
        print(f"{value_c} Celsius is {result_f} Fahrenheit")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
    print("\n--- Error Handling Example ---")
    try:
        manager.convert_value(10, "meter", "kilogram")
    except TypeError as e:
        print(f"Caught expected error: {e}")