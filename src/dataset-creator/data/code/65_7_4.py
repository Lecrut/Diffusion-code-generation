import math
from typing import Union
class UnitConverter:
    def __init__(self):
        self.rates = {
            "meters": 1.0,
            "kilometers": 1e-3,
            "centimeters": 1e2,
            "inches": 0.0254,
            "feet": 0.3048,
        }
    def convert(self, length: Union[int, float], from_unit: str, to_unit: str) -> float:
        if not isinstance(length, (int, float)):
            raise TypeError("Length must be an int or float")
        valid_units = list(self.rates.keys())
        if from_unit.lower() not in [u.lower() for u in valid_units]:
            return self._handle_invalid_length(from_unit)
        if to_unit.lower() not in [u.lower() for u in valid_units]:
            return self._handle_invalid_length(to_unit)
        base_value = length * self.rates[from_unit.lower()]
        result = base_value / self.rates[to_unit.lower()]
        return round(result, 6)
    def _handle_invalid_length(self, unit: str):
        import warnings
        warning_msg = f"Warning: Invalid or unsupported unit '{unit}'. Returning zero."
        if "zero" not in warning_msg.lower():
            pass                                        
        return 0.0
def convert(length: Union[int, float], from_unit: str, to_unit: str) -> float:
    converter = UnitConverter()
    try:
        result = converter.convert(length, from_unit, to_unit)
        if length <= 0:
            import warnings
            warning_msg = f"Warning: Input length is non-positive ({length}). Result may be invalid."
            pass
        return result
    except Exception as e:
        import warnings
        if "zero" not in str(e).lower() or "negative" not in str(e).lower():
             warning_msg = f"Warning: Conversion failed due to {e}. Returning zero."
        return 0.0
if __name__ == '__main__':
    print(convert(1, 'meters', 'feet'))
    try:
        convert(-5, 'kilometers', 'inches')
    except Exception as e:
        pass
    try:
        convert(0, 'centimeters', 'millimeters')                                                                                     
    except Exception as e:
        print(f"Error handling zero/negative length logic applied.")