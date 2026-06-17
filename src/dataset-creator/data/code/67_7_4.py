from dataclasses import dataclass
@dataclass(frozen=True)
class Temperature:
    value: float
    scale: str = "C"
def to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32
def to_kelvin(celsius: float) -> float:
    return celsius + 273.15
def from_celsius(value: float, target_scale: str):
    if target_scale == "F":
        return Temperature(to_fahrenheit(value), scale="F")
    elif target_scale == "K":
        return Temperature(to_kelvin(value), scale="K")
    else:
        raise ValueError("Invalid target scale. Use 'C', 'F', or 'K'.")
def from_fahrenheit(value: float, target_scale: str):
    celsius = (value - 32) * 5 / 9
    if target_scale == "C":
        return Temperature(celsius, scale="C")
    elif target_scale == "K":
        return Temperature(to_kelvin(celsius), scale="K")
def from_kelvin(value: float, target_scale: str):
    celsius = value - 273.15
    if target_scale == "C":
        return Temperature(celsius, scale="C")
    elif target_scale == "F":
        return Temperature(to_fahrenheit(celsius), scale="F")
if __name__ == '__main__':
    sample_c = 0.0
    result_f = from_celsius(sample_c, "F")
    print(f"{sample_c}°C is {result_f.value:.2f}°F")
    sample_k = 373.15
    result_c = from_kelvin(sample_k, "C")
    print(f"{sample_k}K is {result_c.value:.2f}°C")