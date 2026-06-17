import logging
from dataclasses import dataclass
from typing import Literal
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
@dataclass(frozen=True)
class Temperature:
    value: float
    unit: str            
def convert_temperature(temp_in: Temperature, target_unit: str) -> Temperature | None:
    if temp_in.value is not None and isinstance(temp_in.value, (int, float)):
        try:
            celsius = temp_in.value
            if target_unit == 'C':
                return Temperature(value=celsius, unit='C')
            elif target_unit == 'F':
                fahrenheit = (celsius * 9 / 5) + 32
                logger.info(f"Converted {temp_in.unit} to F: {fahrenheit}")
                return Temperature(value=fahrenheit, unit='F')
        except Exception as e:
            logger.error(f"Conversion error for input {temp_in}: {e}", exc_info=True)
    else:
        raise TypeError("Temperature value must be a numeric type.")
def format_output(temp_out: Temperature | None, output_format: Literal['json', 'text'] = 'text') -> str:
    if temp_out is None or not isinstance(temp_out.value, (int, float)):
        return "Conversion failed."
    try:
        value = int(temp_out.value) if isinstance(temp_out.value, float) and temp_out.value.is_integer() else temp_out.value
        if output_format == 'json':
            import json
            result = {"unit": temp_out.unit, "value": value}
            return json.dumps(result)
        elif output_format == 'text':
            unit_symbol = {'C': '°C', 'F': '°F'}.get(temp_out.unit, '')
            formatted_value = f"{value}{unit_symbol}" if isinstance(value, int) else f"{value:.2f}{unit_symbol}"
            return str(formatted_value)
        logger.warning(f"Unsupported output format: {output_format}")
    except Exception as e:
        logger.error(f"Formatting error for temperature {temp_out}: {e}", exc_info=True)
    return "Error occurred."
if __name__ == '__main__':
    sample_input = Temperature(value=25.0, unit='C')
    target_unit = 'F'
    try:
        converted_temp = convert_temperature(sample_input, target_unit)
        if isinstance(converted_temp.value, float):
            formatted_text = format_output(converted_temp, output_format='text')
            logger.info(f"Result (Text): {formatted_text}")
            import json as j
            formatted_json = format_output(converted_temp, output_format='json')
            logger.info(f"Result (JSON): {formatted_json}")
    except Exception as e:
        logger.critical("Fatal error in main execution", exc_info=True)