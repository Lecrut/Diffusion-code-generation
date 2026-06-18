import sys
from typing import Union
def convert_length(value: Union[int, float], from_unit: str, to_unit: str) -> Union[int, float]:
    standard_rates = {
        "meter": 1.0,
        "kilometer": 1000.0,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "mile": 1609.344,
        "yard": 0.9144,
        "foot": 0.3048,
    }
    def get_rate(unit: str) -> float:
        if unit.lower() in standard_rates:
            return standard_rates[unit.lower()]
        user_defined = getattr(sys.modules[__name__], f"USER_RATE_{unit.upper().replace(' ', '_')}", None)
        if callable(user_defined):
            return user_defined(value=1.0)
        raise ValueError(f"No conversion rate found for unit '{unit}'.")
    from_rate = get_rate(from_unit)
    value_in_meters = value * from_rate
    to_rate = get_rate(to_unit)
    result = value_in_meters / to_rate
    return round(result, 6)
def handle_edge_case(value: Union[int, float], unit_type: str):
    if isinstance(value, (int, float)):
        if value == 0:
            print(f"Warning: Zero length input for {unit_type}.")
        elif value < 0:
            print(f"Warning: Negative length input for {unit_type} is not physically meaningful.")
if __name__ == '__main__':
    handle_edge_case(15, "meters")
    def custom_rate(value):
        return value * 2.5
    setattr(sys.modules[__name__], "USER_RATE_CUSTOM_UNIT", custom_rate)
    try:
        result = convert_length(-50, "meter", "foot")
        print(f"Converted -50 meters to {result} feet.")
    except ValueError as e:
        print(e)
    handle_edge_case(0.0, "kilometers")