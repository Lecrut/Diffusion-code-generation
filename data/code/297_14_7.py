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
                return (value * 9/5) + 32
            elif from_unit == "fahrenheit" and to_unit == "celsius":
                return (value - 32) * 5/9
            else:
                raise NotImplementedError("Direct temperature conversion not implemented for this path")
        else:
            raise TypeError("Unsupported unit type for conversion")
        return result
if __name__ == '__main__':
    manager = ConversionManager()
    length_value = 500.0
    from_unit = "meter"
    to_unit = "kilometer"
    result_length = manager.convert_value(length_value, from_unit, to_unit)
    print(f"{length_value} {from_unit} is equal to {result_length} {to_unit}")
    mass_value = 2500.0
    from_unit = "gram"
    to_unit = "kilogram"
    result_mass = manager.convert_value(mass_value, from_unit, to_unit)
    print(f"{mass_value} {from_unit} is equal to {result_mass} {to_unit}")
    temp_celsius = 20.0
    from_unit = "celsius"
    to_unit = "fahrenheit"
    result_temp = manager.convert_value(temp_celsius, from_unit, to_unit)
    print(f"{temp_celsius}°C is equal to {result_temp}°F")
    temp_fahrenheit = 68.0
    from_unit = "fahrenheit"
    to_unit = "celsius"
    result_temp_rev = manager.convert_value(temp_fahrenheit, from_unit, to_unit)
    print(f"{temp_fahrenheit}°F is equal to {result_temp_rev}°C")