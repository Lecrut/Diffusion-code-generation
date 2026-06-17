from abc import ABC, abstractmethod
class Unit(ABC):
    @abstractmethod
    def to_base(self, value: float) -> float:
        pass
    @abstractmethod
    def from_base(self, base_value: float) -> float:
        pass
    @abstractmethod
    def convert(self, value: float, from_unit: 'Unit', to_unit: 'Unit') -> float:
        pass
class Length(Unit):
    def __init__(self, value: float):
        self._value = value
    def to_base(self, value: float) -> float:
        return value
    def from_base(self, base_value: float) -> float:
        return base_value
    def convert(self, value: float, from_unit: 'Unit', to_unit: 'Unit') -> float:
        if isinstance(from_unit, Length) and isinstance(to_unit, Length):
            base_val = from_unit.to_base(value)
            return to_unit.from_base(base_val)
        raise TypeError("Cannot convert between different unit types.")
class Temperature(Unit):
    def __init__(self, value: float):
        self._value = value
    def to_base(self, value: float) -> float:
        return value
    def from_base(self, base_value: float) -> float:
        return base_value
    def convert(self, value: float, from_unit: 'Unit', to_unit: 'Unit') -> float:
        if isinstance(from_unit, Temperature) and isinstance(to_unit, Temperature):
            base_val = from_unit.to_base(value)
            return to_unit.from_base(base_val)
        raise TypeError("Cannot convert between different unit types.")
class ConversionManager:
    def __init__(self):
        self.units = {
            "meter": Length(1.0),
            "kilometer": Length(1000.0),
            "inch": Length(0.0254),
            "foot": Length(0.3048)
        }
        self.temperature_units = {
            "celsius": Temperature(0.0),
            "fahrenheit": Temperature(0.0),
            "kelvin": Temperature(0.0)
        }
    def get_unit(self, unit_name: str):
        if unit_name in self.units:
            return self.units[unit_name]
        if unit_name in self.temperature_units:
            return self.temperature_units[unit_name]
        raise ValueError(f"Unknown unit: {unit_name}")
    def convert_length(self, value: float, from_unit: str, to_unit: str) -> float:
        from_obj = self.get_unit(from_unit)
        to_obj = self.get_unit(to_unit)
        return from_obj.convert(value, from_obj, to_obj)
    def convert_temperature(self, value: float, from_unit: str, to_unit: str) -> float:
        from_obj = self.get_unit(from_unit)
        to_obj = self.get_unit(to_unit)
        return from_obj.convert(value, from_obj, to_obj)
if __name__ == '__main__':
    manager = ConversionManager()
    print("--- Length Conversions ---")
    try:
        length_value = 10.0
        from_unit = "meter"
        to_unit = "kilometer"
        result = manager.convert_length(length_value, from_unit, to_unit)
        print(f"{length_value} {from_unit} is equal to {result} {to_unit}")
        length_value = 10.0
        from_unit = "inch"
        to_unit = "foot"
        result = manager.convert_length(length_value, from_unit, to_unit)
        print(f"{length_value} {from_unit} is equal to {result} {to_unit}")
    except ValueError as e:
        print(f"Error in length conversion: {e}")
    print("\n--- Temperature Conversions ---")
    try:
        temp_value = 20.0
        from_unit = "celsius"
        to_unit = "fahrenheit"
        result = manager.convert_temperature(temp_value, from_unit, to_unit)
        print(f"{temp_value}°C is equal to {result}°F")
        temp_value = 300.0
        from_unit = "kelvin"
        to_unit = "celsius"
        result = manager.convert_temperature(temp_value, from_unit, to_unit)
        print(f"{temp_value}K is equal to {result}°C")
    except ValueError as e:
        print(f"Error in temperature conversion: {e}")