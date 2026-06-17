from dataclasses import dataclass
@dataclass
class Temperature:
    value: float
    scale: str = "C"
def to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32
def to_kelvin(celsius: float) -> float:
    return celsius + 273.15
def from_celsius(value: Temperature) -> Temperature:
    if value.scale == "C":
        new_temp = Temperature(to_fahrenheit(value.value), scale="F")
        print(f"{value.value}°C is {new_temp.value:.2f}°F and {to_kelvin(value.value):.2f}K")
    else:
        raise ValueError("Input must be in Celsius for this example.")
def from_fahrenheit(value: Temperature) -> Temperature:
    if value.scale == "F":
        celsius = (value.value - 32) * 5 / 9
        new_temp = Temperature(celsius, scale="C")
        print(f"{value.value}°F is {new_temp.value:.2f}°C and {to_kelvin(new_temp.value):.2f}K")
    else:
        raise ValueError("Input must be in Fahrenheit for this example.")
def from_kelvin(value: Temperature) -> Temperature:
    if value.scale == "K":
        celsius = value.value - 273.15
        new_temp = Temperature(celsius, scale="C")
        print(f"{value.value}K is {new_temp.value:.2f}°C and {to_fahrenheit(new_temp.value):.2f}°F")
    else:
        raise ValueError("Input must be in Kelvin for this example.")
if __name__ == '__main__':
    sample_c = Temperature(0)
    from_celsius(sample_c)
    sample_f = Temperature(32, scale="F")
    from_fahrenheit(sample_f)
    sample_k = Temperature(273.15, scale="K")
    from_kelvin(sample_k)