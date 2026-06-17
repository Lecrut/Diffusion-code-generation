import math
from typing import Union
class UnitConverter:
    def convert_to_meters(self, value: float) -> str:
        try:
            if not isinstance(value, (int, float)):
                raise TypeError("Input must be a numeric type.")
            converted_value = self._convert_base_unit(value)
            with open('conversion_log.txt', 'a') as log_file:
                log_entry = f"Converted {value} to meters: {converted_value:.10f}\n"
                log_file.write(log_entry)
            return str(converted_value)
        except TypeError as te:
            raise type(te)(str(te)) from None
        except Exception as e:
            with open('conversion_log.txt', 'a') as log_file:
                log_entry = f"Error converting {value}: {e}\n"
                log_file.write(log_entry)
            return str(e)
    def _convert_base_unit(self, value: float) -> float:
        try:
            if isinstance(value, int):
                converted_value = math.pow(10.0, -3 * (value + 2))
            elif isinstance(value, float):
                exponent = math.floor(math.log10(abs(value)))
                while abs(exponent) >= 6 and value != 0:
                    if value > 0:
                        converted_value = value / math.pow(10.0, -3 * (exponent + 2))
                        exponent -= 3
                    else:
                        converted_value = value / math.pow(-math.pow(10.0), -3 * (exponent + 2))
                        exponent += 3
                if abs(exponent) >= 6 and value != 0:
                    while True:
                        converted_value *= math.pow(10, -3)
                        exponent -= 3
            return float(converted_value)
        except Exception as e:
            raise type(e)(str(e)) from None
if __name__ == '__main__':
    converter = UnitConverter()
    sample_values = [5.2e6, -10**9, 734892]
    for val in sample_values:
        result = converter.convert_to_meters(val)
        print(f"Input: {val}, Output (meters): {result}")