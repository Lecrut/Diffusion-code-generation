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
        return self.units.get(unit_name)
    def convert_value(self, value, from_unit, to_unit):
        if from_unit not in self.units or to_unit not in self.units:
            raise ValueError("Invalid unit specified")
        from_obj = self.units[from_unit]
        to_obj = self.units[to_unit]
        base_value = from_obj.to_base(value)
        if isinstance(from_obj, Length):
            result = to_obj.from_base(base_value)
        elif isinstance(from_obj, Mass):
            result = to_obj.from_base(base_value)
        elif isinstance(from_obj, Temperature):
            if from_unit == "celsius" and to_unit == "fahrenheit":
                result = (base_value * 9/5) + 32
            elif from_unit == "fahrenheit" and to_unit == "celsius":
                result = (base_value - 32) * 5/9
            else:
                result = to_obj.from_base(base_value)
        else:
            raise TypeError("Unsupported unit type for conversion")
        return result
if __name__ == '__main__':
    manager = ConversionManager()
    print("--- Length Conversion (Meter to Kilometer) ---")
    length_val = 500.0
    try:
        result_len = manager.convert_value(length_val, "meter", "kilometer")
        print(f"{length_val} meters is {result_len} kilometers")
    except Exception as e:
        print(f"Error: {e}")
    print("\n--- Mass Conversion (Gram to Kilogram) ---")
    mass_val = 2500.0
    try:
        result_mass = manager.convert_value(mass_val, "gram", "kilogram")
        print(f"{mass_val} grams is {result_mass} kilograms")
    except Exception as e:
        print(f"Error: {e}")
    print("\n--- Temperature Conversion (Celsius to Fahrenheit) ---")
    temp_c = 20.0
    try:
        result_temp = manager.convert_value(temp_c, "celsius", "fahrenheit")
        print(f"{temp_c}°C is {result_temp}°F")
    except Exception as e:
        print(f"Error: {e}")
    print("\n--- Temperature Conversion (Fahrenheit to Celsius) ---")
    temp_f = 68.0
    try:
        result_temp_rev = manager.convert_value(temp_f, "fahrenheit", "celsius")
        print(f"{temp_f}°F is {result_temp_rev}°C")
    except Exception as e:
        print(f"Error: {e}")
    print("\n--- Length Conversion (Kilometer to Meter) ---")
    length_val_2 = 2.5
    try:
        result_len_2 = manager.convert_value(length_val_2, "kilometer", "meter")
        print(f"{length_val_2} kilometers is {result_len_2} meters")
    except Exception as e:
        print(f"Error: {e}")