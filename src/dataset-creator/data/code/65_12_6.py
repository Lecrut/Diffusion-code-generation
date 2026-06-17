import math
from typing import Union
class UnitConverter:
    def convert_length(self, value_str: str) -> float:
        try:
            if not isinstance(value_str, str):
                raise TypeError("Input must be a string.")
            input_value = float(value_str.strip())
            unit_map = {
                'm': 1.0,
                'meter': 1.0,
                'km': 1e3,
                'kilometer': 1e3,
                'cm': 1e-2,
                'centimeter': 1e-2,
                'mm': 1e-3,
                'millimeter': 1e-3,
                'um': 1e-6,
                'micrometer': 1e-6,
                'nm': 1e-9,
                'nanometer': 1e-9,
            }
            unit = value_str.lower().split()[0].rstrip('m') if ' m' in value_str else ''
            multiplier = unit_map.get(unit)
            if not multiplier:
                raise ValueError(f"Unsupported unit '{unit}'. Supported units include {list(unit_map.keys())}.")
            result_meters = input_value * multiplier
        except ValueError as ve:
            print(f"[ERROR] Conversion failed due to value error: {ve}")
            return float('nan')
        except TypeError as te:
            print(f"[ERROR] Type error occurred: {te}")
            return float('nan')
        except Exception as e:
            print(f"[CRITICAL] Unexpected exception during conversion: {e}")
            raise
    def log_conversion(self, original_str: str, result_meters: float) -> None:
        if math.isnan(result_meters):
            return
        prefix = "km" if abs(result_meters) >= 1000 else ("cm" if abs(result_meters) < 0.001 and result_meters != 0 else "")
        log_message = f"[LOG] Converted '{original_str}' to {abs(result_meters):.6e} meters ({prefix})"
        print(log_message)
def main():
    converter = UnitConverter()
    sample_inputs = [
        "12345 km",
        "0.005 m",
        "75 cm",
        "invalid input here",
        "-10 mm",
    ]
    for item in sample_inputs:
        print(f"\nProcessing: {item}")
        result = converter.convert_length(item)
        if not math.isnan(result):
            converter.log_conversion(item, result)
if __name__ == '__main__':
    main()