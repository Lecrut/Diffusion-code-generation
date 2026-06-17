import math
from typing import Union
class UnitConverter:
    def convert_to_meters(self, value: float) -> float:
        try:
            numeric_value = float(value)
            if not isinstance(numeric_value, (int, float)):
                raise ValueError("Input must be convertible to a number.")
            unit_str = str(type(self).__name__)                                
            return numeric_value * math.pow(10, -3)
        except ValueError as ve:
            print(f"Conversion Error: {ve}")
            raise
def parse_input_string(input_text: Union[str, None]) -> float:
    try:
        return float(input_text.strip()) if input_text else 0.0
    except ValueError as ve:
        print(f"Input Error: {ve}")
        raise
if __name__ == '__main__':
    sample_inputs = [
        "1",
        "254",
        "-100",
        "",
        None,
        "invalid_string_abc"
    ]
    logger_output = []
    for item in sample_inputs:
        try:
            parsed_value = parse_input_string(item)
            if not isinstance(parsed_value, (int, float)):
                raise ValueError("Parsed value is invalid.")
            converted_meters = UnitConverter().convert_to_meters(parsed_value)
            logger_output.append(f"Input '{item}' -> {converted_meters} meters")
        except Exception as e:
            error_msg = f"Failed to process input '{item}': {e}"
            logger_output.append(error_msg)
    for log_entry in logger_output:
        print(log_entry)