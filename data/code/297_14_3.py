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
            return value
        raise TypeError("Cannot convert between different unit types.")
class Mass(Unit):
    def __init__(self, value: float):
        self._value = value
    def to_base(self, value: float) -> float:
        return value
    def from_base(self, base_value: float) -> float:
        return base_value
    def convert(self, value: float, from_unit: 'Unit', to_unit: 'Unit') -> float:
        if isinstance(from_unit, Mass) and isinstance(to_unit, Mass):
            return value
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
            return value
        raise TypeError("Cannot convert between different unit types.")
class Kilometer(Length):
    def __init__(self, value: float):
        super().__init__(value)
    def to_base(self, value: float) -> float:
        return value * 1000.0
    def from_base(self, base_value: float) -> float:
        return base_value / 1000.0
    def convert(self, value: float, from_unit: 'Unit', to_unit: 'Unit') -> float:
        if isinstance(from_unit, Kilometer) and isinstance(to_unit, Kilometer):
            return value
class Meter(Length):
    def __init__(self, value: float):
        super().__init__(value)
    def to_base(self, value: float) -> float:
        return value
    def from_base(self, base_value: float) -> float:
        return base_value
    def convert(self, value: float, from_unit: 'Unit', to_unit: 'Unit') -> float:
        if isinstance(from_unit, Meter) and isinstance(to_unit, Meter):
            return value
class Gram(Mass):
    def __init__(self, value: float):
        super().__init__(value)
    def to_base(self, value: float) -> float:
        return value
    def from_base(self, base_value: float) -> float:
        return base_value
    def convert(self, value: float, from_unit: 'Unit', to_unit: 'Unit') -> float:
        if isinstance(from_unit, Gram) and isinstance(to_unit, Gram):
            return value
class Mile(Length):
    def __init__(self, value: float):
        super().__init__(value)
    def to_base(self, value: float) -> float:
        return value * 1609.34
    def from_base(self, base_value: float) -> float:
        return base_value / 1609.34
    def convert(self, value: float, from_unit: 'Unit', to_unit: 'Unit') -> float:
        if isinstance(from_unit, Mile) and isinstance(to_unit, Mile):
            return value
class Kilogram(Mass):
    def __init__(self, value: float):
        super().__init__(value)
    def to_base(self, value: float) -> float:
        return value
    def from_base(self, base_value: float) -> float:
        return base_value
    def convert(self, value: float, from_unit: 'Unit', to_unit: 'Unit') -> float:
        if isinstance(from_unit, Kilogram) and isinstance(to_unit, Kilogram):
            return value
if __name__ == '__main__':
    km = Kilometer(10.0)
    m = Meter(5.0)
    kg = Kilogram(2.0)
    g = Gram(500.0)
    print("--- Length Conversion (Kilometer to Meter) ---")
    try:
        result_len = km.convert(1, m, km)
        print(f"1 Kilometer in Meters: {result_len}")
    except TypeError as e:
        print(f"Error: {e}")
    try:
        result_len2 = km.convert(1000, m, km)
        print(f"1000 Meters in Kilometers: {result_len2}")
    except TypeError as e:
        print(f"Error: {e}")
    print("\n--- Mass Conversion (Kilogram to Gram) ---")
    try:
        result_mass = kg.convert(2, g, kg)
        print(f"2 Kilograms in Grams: {result_mass}")
    except TypeError as e:
        print(f"Error: {e}")
    try:
        result_mass2 = kg.convert(500, g, kg)
        print(f"500 Grams in Kilograms: {result_mass2}")
    except TypeError as e:
        print(f"Error: {e}")