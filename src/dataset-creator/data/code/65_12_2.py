import math
from typing import Union
class UnitConverter:
    def convert_to_meters(self, value: float, unit: str) -> float:
        conversion_factors = {
            'm': 1.0,
            'km': 1_000.0,
            'cm': 0.01,
            'mm': 0.001,
            'um': 1e-6,
            'nm': 1e-9,
        }
        if unit.lower() not in conversion_factors:
            raise ValueError(f"Unsupported unit '{unit}'. Supported units are {list(conversion_factors.keys())}.")
        try:
            return value * conversion_factors[unit.lower()]
        except OverflowError as e:
            print(f"[ERROR] Numeric overflow occurred during calculation. Details: {e}")
            raise
def log_message(level: str, message: str) -> None:
    prefix = f"[{level}]" if level != "INFO" else "[I]"
    print(f"{prefix}: {message}")
if __name__ == '__main__':
    converter = UnitConverter()
    test_cases = [
        (1, 'km'),
        (500, 'cm'),
        (-2.5, 'm'),
        (3e6, 'um'),
        ('invalid', 'm'),                                                                                                   
    ]
    log_message("INFO", "Starting unit conversion process.")
    for value_str, unit in test_cases:
        try:
            value = float(value_str)
            result = converter.convert_to_meters(value, unit)
            log_message("DEBUG", f"Converted {value} {unit} to meters: {result}")
        except ValueError as ve:
            if isinstance(value_str, str):
                print(f"[ERROR] Invalid input type for value. Expected numeric string.")
            else:
                raise ve
        except Exception as e:
            log_message("CRITICAL", f"Unexpected error occurred while processing {value} {unit}. Error: {e}")
    log_message("INFO", "Conversion process completed successfully.")