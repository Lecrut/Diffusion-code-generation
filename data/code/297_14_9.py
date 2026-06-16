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
        raise TypeError("Cannot convert length to another type")
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
        raise TypeError("Cannot convert mass to another type")
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
        raise TypeError("Cannot convert temperature to another type")
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
        return self.units.get(unit_name)
    def convert_value(self, value, from_unit, to_unit):
        if from_unit not in self.units or to_unit not in self.units:
            raise ValueError("Invalid unit specified")
        from_obj = self.units[from_unit]
        to_obj = self.units[to_unit]
        if isinstance(from_obj, Length) and isinstance(to_obj, Length):
            base_val = from_obj.to_base(value)
            return to_obj.from_base(base_val)
        elif isinstance(from_obj, Mass) and isinstance(to_obj, Mass):
            base_val = from_obj.to_base(value)
            return to_obj.from_base(base_val)
        elif isinstance(from_obj, Temperature) and isinstance(to_obj, Temperature):
            base_val = from_obj.to_base(value)
            return to_obj.from_base(base_val)
        else:
            raise TypeError("Unit types are incompatible for conversion")
if __name__ == '__main__':
    manager = ConversionManager()
    print("--- Length Conversion (Meter to Kilometer) ---")
    try:
        length_value = 500.0
        from_unit = "meter"
        to_unit = "kilometer"
        result = manager.convert_value(length_value, from_unit, to_unit)
        print(f"{length_value} {from_unit} is equal to {result} {to_unit}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
    print("\n--- Mass Conversion (Gram to Kilogram) ---")
    try:
        mass_value = 2500.0
        from_unit = "gram"
        to_unit = "kilogram"
        result = manager.convert_value(mass_value, from_unit, to_unit)
        print(f"{mass_value} {from_unit} is equal to {result} {to_unit}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
    print("\n--- Temperature Conversion (Celsius to Fahrenheit) ---")
    try:
        temp_value = 20.0
        from_unit = "celsius"
        to_unit = "fahrenheit"
        result = manager.convert_value(temp_value, from_unit, to_unit)
        print(f"{temp_value}°C is equal to {result}°F")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
    print("\n--- Attempting Invalid Conversion ---")
    try:
        manager.convert_value(10, "meter", "gram")
    except (ValueError, TypeError) as e:
        print(f"Caught expected error: {e}")