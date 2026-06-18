from dataclasses import dataclass
@dataclass(frozen=True)
class Temperature:
    value: float
    scale: str = "C"
    def to_fahrenheit(self) -> float:
        return (self.value * 9 / 5) + 32
    def to_kelvin(self) -> float:
        return self.value + 273.15
@dataclass(frozen=True)
class Celsius(Temperature):
    scale = "C"
@dataclass(frozen=True)
class Fahrenheit(Temperature):
    value: float
    scale = "F"
    def to_celsius(self) -> float:
        return (self.value - 32) * 5 / 9
    def to_kelvin(self) -> float:
        celsius = self.to_celsius()
        return celsius + 273.15
@dataclass(frozen=True)
class Kelvin(Temperature):
    value: float
    scale = "K"
    def to_celsius(self) -> float:
        return self.value - 273.15
    def to_fahrenheit(self) -> float:
        celsius = self.to_celsius()
        return (celsius * 9 / 5) + 32
if __name__ == '__main__':
    temp_c = Celsius(0)
    print(f"{temp_c.value}°C is {temp_c.to_fahrenheit():.1f}°F and {temp_c.to_kelvin():.1f}K")
    temp_f = Fahrenheit(32)
    print(f"{temp_f.value}°F is {temp_f.to_celsius():.1f}°C and {temp_f.to_kelvin():.1f}K")
    temp_k = Kelvin(0)
    print(f"{temp_k.value}K is {temp_k.to_celsius():.1f}°C and {temp_k.to_fahrenheit():.1f}°F")