import sys
from typing import Union, Dict, Any
def convert_length(value: Union[int, float], from_unit: str, to_unit: str) -> Union[float, int]:
    standard_rates = {
        "m": 1.0,
        "km": 1000.0,
        "cm": 0.01,
        "mm": 0.001,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
    }
    def get_rate(unit: str) -> float:
        if unit in standard_rates:
            return standard_rates[unit]
        elif user_defined.get(unit):
            return user_defined[unit]
        else:
            raise ValueError(f"Unknown unit: {unit}")
    from_factor = get_rate(from_unit.lower())
    to_factor = get_rate(to_unit.lower())
    if value <= 0:
        print("Warning: Zero or negative length provided.")
        return float(value) * (to_factor / from_factor)
    converted_value = value * (to_factor / from_factor)
    if isinstance(value, int):
        return round(converted_value)
    else:
        return converted_value
user_defined: Dict[str, Union[int, float]] = {}
if __name__ == '__main__':
    sample_input_1 = convert_length(5.0, "ft", "m")
    print(f"Result 1: {sample_input_1}")
    sample_input_2 = convert_length(10, "in", "cm")
    print(f"Result 2: {sample_input_2}")
    try:
        result_zero = convert_length(0, "m", "km")
        print(f"Zero Result: {result_zero}")
    except Exception as e:
        print(e)
    sample_input_3 = convert_length(-1.5, "ft", "in")
    print(f"Negative Result: {sample_input_3}")