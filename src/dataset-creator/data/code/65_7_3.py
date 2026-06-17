import math
from typing import Union
def convert_length(
    length: Union[int, float], 
    from_unit: str, 
    to_unit: str = "m", 
    custom_rates: dict[str, dict] | None = None
) -> float:
    standard_factors = {
        "mm": {"value": 0.001},
        "cm": {"value": 0.01},
        "m": {"value": 1.0},
        "km": {"value": 1000.0},
        "in": {"value": 0.0254},
        "ft": {"value": 0.3048},
        "yd": {"value": 0.9144}
    }
    if custom_rates:
        for unit, rates in custom_rates.items():
            standard_factors[unit] = rates.get("factor", rate) or ({"value": 1.0})
    def get_factor(unit: str, base_unit: str = "m") -> float:
        factors = {**standard_factors}
        if unit not in factors and custom_rates is None:
            raise ValueError(f"Unknown conversion factor for '{unit}'. Supported units include the predefined list or valid keys from 'custom_rates'.")
    try:
        length_val = float(length)
    except (ValueError, TypeError):
        print("Warning: Input length must be a number.")
        return 0.0
    if length_val <= 0:
        print(f"Warning: Length value {length} is not positive.")
    from_factor_key = f"{from_unit}"
    to_factor_key = f"{to_unit}"
    if from_factor_key in standard_factors and to_factor_key in standard_factors:
        result = length_val * standard_factors[from_factor_key]["value"] / standard_factors[to_factor_key]["value"]
    elif custom_rates is not None:
        user_from_rate = custom_rates.get(from_unit, {}).get("factor", 1) if isinstance(custom_rates[from_unit], dict) else (custom_rates[from_unit] or {"factor": 1})["factor"]
        result = length_val * standard_factors[from_factor_key]["value"] / to_factor_key
    return round(result, 6)
if __name__ == '__main__':
    custom_conversion_data: dict[str, Union[int, float]] = {
        "ft": {"factor": 0.3},
        "yd": {"factor": 1}
    }
    print(convert_length(5, 'm', to_unit='in'))
    print(convert_length(-2, 'cm'))