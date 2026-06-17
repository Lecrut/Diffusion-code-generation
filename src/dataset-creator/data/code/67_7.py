from dataclasses import dataclass
@dataclass
class Temperature:
    value: float
    scale: str = "celsius"
    def to_fahrenheit(self) -> 'Temperature':
        return Temperature((self.value * 9 / 5) + 32, "fahrenheit")
    def to_kelvin(self) -> 'Temperature':
        return Temperature(self.value + 273.15, "kelvin")
@dataclass
class CelsiusConverter:
    celsius_value: float
    @property
    def fahrenheit(self) -> float:
        return (self.celsius_value * 9 / 5) + 32
    @property
    def kelvin(self) -> float:
        return self.celsius_value + 273.15
@dataclass
class FahrenheitConverter:
    fahrenheit_value: float
    @property
    def celsius(self) -> float:
        return (self.fahrenheit_value - 32) * 5 / 9
    @property
    def kelvin(self) -> float:
        return self.fahrenheit_value + 459.67
@dataclass
class KelvinConverter:
    kelvin_value: float
    @property
    def celsius(self) -> float:
        return self.kelvin_value - 273.15
    @property
    def fahrenheit(self) -> float:
        return (self.kelvin_value + 459.67) * 9 / 5
if __name__ == '__main__':
    c_temp = CelsiusConverter(celsius_value=20)
    print(f"Celsius to Fahrenheit: {c_temp.fahrenheit}")
    print(f"Celsius to Kelvin: {c_temp.kelvin}")
    f_temp = FahrenheitConverter(fahrenheit_value=68)
    print(f"Fahrenheit to Celsius: {f_temp.celsius}")
    print(f"Fahrenheit to Kelvin: {f_temp.kelvin}")
    k_temp = KelvinConverter(kelvin_value=293.15)
    print(f"Kelvin to Celsius: {k_temp.celsius}")
    print(f"Kelvin to Fahrenheit: {k_temp.fahrenheit}")