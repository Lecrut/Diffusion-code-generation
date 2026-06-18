import logging
from dataclasses import dataclass
from typing import Literal
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
@dataclass(frozen=True)
class Temperature:
    value: float
    unit: str            
def convert_temperature(source_temp: Temperature, target_unit: str) -> Temperature | None:
    if not isinstance(source_temp.value, (int, float)):
        raise TypeError("Temperature value must be numeric.")
    celsius = 0.0
    if source_temp.unit == 'C':
        celsius = source_temp.value
    elif source_temp.unit == 'F':
        celsius = (source_temp.value - 32) * 5 / 9
    else:
        raise ValueError(f"Unsupported unit '{source_temp.unit}'.")
    if target_unit not in ('C', 'F'):
        return None
    result_celsius = celsius
    if target_unit == 'C':
        result_fahrenheit = (result_celsius * 9 / 5) + 32
        logger.info(f"Converted {source_temp.value}°{source_temp.unit} to {result_fahrenheit:.2f}°F")
        return Temperature(value=result_fahrenheit, unit='F')
    if target_unit == 'F':
        result_celsius = celsius
        logger.info(f"Converted {source_temp.value}°{source_temp.unit} to {result_celsius:.2f}°C")
        return Temperature(value=result_celsius, unit='C')
def format_output(temp: Temperature | None) -> str:
    if temp is None:
        return "Conversion failed."
    formatted = f"{temp.value:.2f}°{temp.unit}"
    logger.info(f"Formatted result: {formatted}")
    return formatted
if __name__ == '__main__':
    sample_temp_celsius = Temperature(value=100.5, unit='C')
    target_unit = 'F'
    converted_result = convert_temperature(sample_temp_celsius, target_unit)
    if converted_result:
        output_string = format_output(converted_result)
        print(output_string)
        try:
            bad_input = Temperature(value="invalid", unit='C')
            convert_temperature(bad_input, 'F')
        except TypeError as e:
            logger.error(f"Caught expected error for type safety check: {e}")
    result_none = convert_temperature(sample_temp_celsius, 'K')
    print(format_output(result_none))