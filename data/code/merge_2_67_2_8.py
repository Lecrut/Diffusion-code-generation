from typing import Optional
def celsius_to_fahrenheit(c: float) -> float:
    return c * 18 / 10 + 32
def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32.0) * 5 / 9
def celsius_to_kelvin(c: float) -> float:
    return c + 273.15
def kelvin_to_celsius(k: float) -> float:
    return k - 273.15
if __name__ == '__main__':
    sample_values = {
        "celsius": [0, 100],
        "fahrenheit": [-40, 212]
    }
    c_temp: float | None = next(iter(sample_values["celsius"])) if sample_values.get("celsius") else None
    f_temp: float | None = next(iter(sample_values["fahrenheit"])) if sample_values.get("fahrenheit") else None
    result_c_to_f: Optional[float] = celsius_to_fahrenheit(c_temp) if c_temp is not None else None
    result_f_to_c: Optional[float] = fahrenheit_to_celsius(f_temp) if f_temp is not None else None
    result_k_from_c: float | None = celsius_to_kelvin(c_temp) if c_temp is not None else None
    print("Celsius to Fahrenheit:", result_c_to_f)
    print("Fahrenheit to Celsius:", result_f_to_c)
    print("Kelvin from Celsius:", result_k_from_c)