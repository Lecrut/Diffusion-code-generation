from abc import ABC, abstractmethod
class Unit(ABC):
    @abstractmethod
    def to_base(self, value: float) -> float:
        pass
    @abstractmethod
    def from_base(self, base_value: float) -> float:
        pass
    @abstractmethod
    def __str__(self) -> str:
        pass
class Length(Unit):
    def to_base(self, value: float) -> float:
        return value
    def from_base(self, base_value: float) -> float:
        return base_value
    def __str__(self) -> str:
        return "Length"
class Mass(Unit):
    def to_base(self, value: float) -> float:
        return value
    def from_base(self, base_value: float) -> float:
        return base_value
    def __str__(self) -> str:
        return "Mass"
class Temperature(Unit):
    def to_base(self, value: float) -> float:
        return value
    def from_base(self, base_value: float) -> float:
        return base_value
    def __str__(self) -> str:
        return "Temperature"
class ConversionSystem:
    def convert(self, value: float, from_unit: Unit, to_unit: Unit) -> float:
        if not isinstance(from_unit, type) or not isinstance(to_unit, type):
            raise TypeError("Units must be classes.")
        if type(from_unit) is not type(to_unit):
            raise ValueError("Cannot convert between different unit types (e.g., Length to Mass).")
        if isinstance(from_unit, Length) and isinstance(to_unit, Length):
            return value
        elif isinstance(from_unit, Mass) and isinstance(to_unit, Mass):
            return value
        elif isinstance(from_unit, Temperature) and isinstance(to_unit, Temperature):
            return value
        else:
            raise NotImplementedError("Conversion logic not implemented for this unit pair.")
if __name__ == '__main__':
    system = ConversionSystem()
    length_value = 10.0
    mass_value = 5.0
    temp_value = 25.0
    print(f"--- Length Conversion ---")
    try:
        result_len = system.convert(length_value, Length, Length)
        print(f"{length_value} {Length.__name__} to {Length.__name__}: {result_len}")
    except Exception as e:
        print(f"Error: {e}")
    print(f"\n--- Mass Conversion ---")
    try:
        result_mass = system.convert(mass_value, Mass, Mass)
        print(f"{mass_value} {Mass.__name__} to {Mass.__name__}: {result_mass}")
    except Exception as e:
        print(f"Error: {e}")
    print(f"\n--- Temperature Conversion ---")
    try:
        result_temp = system.convert(temp_value, Temperature, Temperature)
        print(f"{temp_value} {Temperature.__name__} to {Temperature.__name__}: {result_temp}")
    except Exception as e:
        print(f"Error: {e}")
    print(f"\n--- Invalid Conversion Attempt ---")
    try:
        system.convert(10, Length, Mass)
    except ValueError as e:
        print(f"Caught expected error: {e}")
    except Exception as e:
        print(f"Caught unexpected error: {e}")