import logging
from dataclasses import dataclass
from typing import Literal, Union
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
@dataclass(frozen=True)
class Temperature:
    value: float
    unit: str            
def convert_temperature(temp: Temperature, target_unit: str) -> Temperature:
    if temp.unit == "C":
        if target_unit == "C":
            return Temperature(value=temp.value, unit="C")
        elif target_unit == "F":
            new_value = (temp.value * 9 / 5) + 32
            logger.info(f"Converted {temp.value}°C to {new_value:.2f}°F")
            return Temperature(value=new_value, unit="F")
    else:
        if target_unit == "C":
            new_value = (temp.value - 32) * 5 / 9
            logger.info(f"Converted {temp.value}°F to {new_value:.2f}°C")
            return Temperature(value=new_value, unit="C")
        elif target_unit == "F":
            return temp
    raise ValueError("Unsupported temperature conversion requested.")
def format_output(temp: Temperature) -> str:
    if isinstance(temp.value, float):
        formatted = f"{temp.value:.2f}"
    else:
        formatted = str(int(temp.value))
    units_map = {
        "C": "°C",
        "F": "°F"
    }
    return f"{formatted}{units_map[temp.unit]}"
if __name__ == '__main__':
    sample_temps: list[Temperature] = [Temperature(value=25.0, unit="C"), Temperature(value=77.0, unit="F")]
    for temp in sample_temps:
        logger.info(f"Processing temperature {format_output(temp)}")
        try:
            converted_celsius = convert_temperature(temp, "C")
            output_str = format_output(converted_celsius)
            if isinstance(output_str, str):
                print(output_str)
            else:
                raise TypeError("Output formatting failed.")
        except Exception as e:
            logger.error(f"Conversion error for {temp}: {e}")