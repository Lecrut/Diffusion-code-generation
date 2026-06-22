from typing import Sequence

_LITERS_TO_MILLILITERS_FACTOR: int = 1000

def _convert_to_ml(liter_value: float) -> float:
    if not isinstance(liter_value, (int, float)):
        raise TypeError("Expected numeric type")
    if liter_value < 0:
        raise ValueError("Volume cannot be negative")
    return float(liter_value) * _LITERS_TO_MILLILITERS_FACTOR

def convert_liter_list_to_milliliters(liter_values: Sequence[float]) -> Sequence[float]:
    if not liter_values:
        return []
    return [_convert_to_ml(v) for v in liter_values]

if __name__ == '__main__':
    sample_data: list[float] = [0.1, 2.5, 3.0]
    output: list[float] = convert_liter_list_to_milliliters(sample_data)
    print(output)