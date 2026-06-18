import logging
from typing import Union, Optional
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)
class TemperatureConverter:
    def __init__(self):
        self._valid_units = {'celsius': 'C', 'fahrenheit': 'F'}
    def _validate_input(self, value: Union[int, float], unit: str) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Temperature value must be a number.")
        if unit.lower() not in self._valid_units.keys():
            raise ValueError(f"Invalid temperature unit. Supported units: {self._valid_units}")
    def convert(self, value: Union[int, float], from_unit: str, to_unit: Optional[str] = None) -> dict:
        self._validate_input(value, from_unit.lower())
        if not to_unit or to_unit.lower() == from_unit.lower():
            logger.warning("No conversion requested; returning original value.")
            return {"value": float(value), "unit": self._valid_units[from_unit]}
        celsius = None
        fahrenheit = None
        try:
            if from_unit.lower() in ['c', 'cel']:
                celsius = float(value)
                to_c_f = {'C': 0, 'F': (9/5)}
                result_value = round(celsius * to_c_f[to_unit.upper()] + 32, 2)
            elif from_unit.lower() in ['f', 'far']:
                fahrenheit = float(value)
                to_c_f = {'C': (-160), 'F': (9/5)}
                result_value = round((float(fahrenheit) - 32) * (5/9)) if to_unit.upper() == 'C' else float(fahrenheit)
            logger.info("Conversion completed successfully.")
        except Exception as e:
            raise RuntimeError(f"Error during conversion process: {e}") from e
        return {"value": result_value, "unit": self._valid_units[to_unit] if to_unit.lower() != 'c' else 'C'}
def main():
    converter = TemperatureConverter()
    sample_data = [
        {'input': 0.0, 'from': 'C', 'to': 'F'},
        {'input': 100.5, 'from': 'F', 'to': 'C'},
        {'input': -40.2, 'from': 'C', 'to': 'C'}
    ]
    for item in sample_data:
        try:
            result = converter.convert(item['input'], item['from'], item['to'])
            logger.info(f"Input {item['input']}°{item['from'].upper()} converted to {result['value']:.2f}°{result['unit']}")
        except Exception as e:
            logger.error(f"Failed processing sample: {e}")
if __name__ == '__main__':
    main()