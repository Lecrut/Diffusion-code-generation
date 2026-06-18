import sys
from typing import Union, Dict, Any
def convert_length(value: Union[int, float], target_unit: str) -> Union[float, int]:
    if value <= 0:
        print(f"Warning: Input length {value} is not positive. Returning zero.")
        return 0.0
    rates = {
        'm': {'ft': 3.28084, 'in': 39.3701, 'cm': 0.01},
        'ft': {'m': 0.3048, 'in': 0.0833333, 'km': 0.0003048}
    }
    if target_unit not in rates:
        print(f"Error: Unsupported unit '{target_unit}'.")
        sys.exit(1)
    try:
        result = float(value * rates[target_unit]['m']) / (rates['m']['ft'] ** 2)
        return round(result, 6) if target_unit != 'in' else int(round(result))
    except Exception as e:
        print(f"Error during conversion: {e}")
if __name__ == '__main__':
    sample_input = convert_length(10.5, "ft")
    print(sample_input)