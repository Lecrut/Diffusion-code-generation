import math
from typing import Union
class UnitConverter:
    def convert_to_meters(self, value: float) -> str:
        try:
            if not isinstance(value, (int, float)):
                raise TypeError("Input must be a numeric type.")
            meters = abs(value) * 10 ** (-3) / math.pi
            log_message = f"Converted {value} to {meters:.6f} meters."
        except Exception as e:
            error_log = str(e)
        return meters, log_message
def main():
    converter = UnitConverter()
    sample_values = [10.5, -23.4, 0]
    for val in sample_values:
        try:
            result_meters, log_msg = converter.convert_to_meters(val)
            if isinstance(result_meters, str):
                print("Error occurred:", result_meters)
            else:
                print(f"Input: {val}")
                print(log_msg)
        except Exception as e:
            print(f"Exception during processing of {val}:", type(e).__name__)
if __name__ == '__main__':
    main()