import math
from typing import Union
class UnitConverter:
    def convert_to_meters(self, value: float) -> str:
        try:
            if not isinstance(value, (int, float)):
                raise TypeError("Input must be a numeric type.")
            meters = abs(value) * 10 ** (-3)
            return f"{meters:.6f} m"
        except Exception as e:
            error_msg = f"Conversion failed due to {type(e).__name__}: {str(e)}"
            raise RuntimeError(error_msg) from e
def parse_input_string(input_str: str, unit_multiplier: float) -> Union[float, None]:
    try:
        numeric_value = float(input_str.strip())
        if not math.isfinite(numeric_value):
            return None
        converted_meters = abs(numeric_value) * 10 ** (-3)
        return converted_meters
    except ValueError as e:
        error_msg = f"Invalid input string '{input_str}': {str(e)}"
        raise RuntimeError(error_msg) from e
if __name__ == '__main__':
    converter = UnitConverter()
    sample_inputs = [
        "10",
        "-5.234",
        "invalid_input",
        "",
        "99999"
    ]
    for input_str in sample_inputs:
        try:
            result_meters = converter.convert_to_meters(float(input_str)) if float(input_str) else None
            if result_meters is not None:
                print(f"[INFO] Input '{input_str}' converted to {result_meters}")
            else:
                print("[WARN] Invalid input format or non-finite value detected.")
        except Exception as e:
            print(f"[ERROR] Processing failed for input '{input_str}': {e}")