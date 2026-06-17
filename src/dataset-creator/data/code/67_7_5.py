from dataclasses import dataclass
@dataclass
class Temperature:
    value: float
    scale: str = 'C'
def to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32
def to_kelvin(celsius: float) -> float:
    return celsius + 273.15
def from_celsius(value: Temperature) -> Temperature:
    if value.scale == 'C':
        new_temp = Temperature(to_fahrenheit(value.value), scale='F')
        print(f"{value.value}°C is {new_temp.value:.2f}°F")
        return new_temp
    elif value.scale == 'F':
        celsius_val = (value.value - 32) * 5 / 9
        kelvin_val = to_kelvin(celsius_val)
        print(f"{value.value}°F is {kelvin_val:.2f}K")
        return Temperature(kelvin_val, scale='K')
    elif value.scale == 'K':
        celsius_val = value.value - 273.15
        fahrenheit_val = to_fahrenheit(celsius_val)
        print(f"{value.value}K is {fahrenheit_val:.2f}°F")
        return Temperature(fahrenheit_val, scale='F')
if __name__ == '__main__':
    temp_c = Temperature(0.0, 'C')
    from_celsius(temp_c)
    temp_f = Temperature(32.0, 'F')
    from_celsius(temp_f)
    temp_k = Temperature(273.15, 'K')
    from_celsius(temp_k)