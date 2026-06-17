from dataclasses import dataclass
@dataclass
class Temperature:
    celsius: float = 0.0
    def to_fahrenheit(self) -> float:
        return (self.celsius * 9 / 5) + 32
    def to_kelvin(self) -> float:
        return self.celsius + 273.15
if __name__ == '__main__':
    temp = Temperature(celsius=0)
    print(f"{temp}°C")
    print(f"= {temp.to_fahrenheit()}°F")
    print(f"= {temp.to_kelvin()}K")