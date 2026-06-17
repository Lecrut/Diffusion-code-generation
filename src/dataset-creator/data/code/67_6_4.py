import logging
from dataclasses import dataclass
from typing import Literal, Union
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
@dataclass(frozen=True)
class Temperature:
    value: float
    unit: str            
def convert_temperature(source_temp: Temperature, target_unit: str) -> Temperature:
    if source_temp.unit == "C":
        converted_value = (source_temp.value * 9 / 5) + 32
        return Temperature(value=converted_value, unit=target_unit)
    elif source_temp.unit == "F":
        converted_value = ((source_temp.value - 32) * 5 / 9)
        return Temperature(value=converted_value, unit=target_unit)
    else:
        raise ValueError(f"Unsupported temperature conversion to {target_unit}")
def format_output(temp: Temperature, output_format: Literal["json", "text"]) -> str:
    if output_format == "json":
        import json
        return json.dumps({"value": temp.value, "unit": temp.unit})
    else:
        return f"{temp.value:.2f} {temp.unit}"
def main():
    sample_temp = Temperature(value=100.5, unit="C")
    logger.info("Starting temperature conversion process.")
    target_units = ["F", "K"]
    output_formats = ["json", "text"]
    for target_unit in target_units:
        converted_result = convert_temperature(sample_temp, target_unit)
        for fmt in output_formats:
            formatted_str = format_output(converted_result, fmt)
            if fmt == "json":
                logger.info(f"JSON Output ({target_unit}): {formatted_str}")
            else:
                print(formatted_str)
    logger.info("Temperature conversion process completed successfully.")
if __name__ == '__main__':
    main()