import logging
from dataclasses import dataclass
from typing import Literal
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
@dataclass(frozen=True)
class Temperature:
    value: float
    unit: str
    @property
    def to_celsius(self) -> float:
        if self.unit == "C":
            return self.value
        elif self.unit == "F":
            return (self.value - 32) * 5 / 9
        else:
            raise ValueError(f"Unsupported unit {self.unit}")
@dataclass(frozen=True)
class ConversionConfig:
    input_unit: str = Literal["C", "F"]
    output_format: Literal["text", "json"] = "text"
    def convert(self, temp: Temperature) -> float | dict[str, any]:
        celsius = temp.to_celsius
        if self.output_format == "json":
            return {
                "input_value": temp.value,
                "input_unit": temp.unit,
                "celsius": round(celsius, 2),
                "output_value": round(temp.value - (32 * celsius / 5) + 32 if self.input_unit == 'F' else celsius, 2),                                                                                         
            }
        return f"{temp.value} {temp.unit} = {round(celsius, 2)} C"
def main():
    config = ConversionConfig(input_unit="C", output_format="json")
    sample_temp_c = Temperature(value=75.0, unit="F")
    sample_temp_f = Temperature(value=38.6, unit="C")
    logger.info("Processing Fahrenheit to Celsius conversion.")
    result1 = config.convert(sample_temp_c)
    if isinstance(result1, dict):
        print(f"Result: {result1}")
    else:
        print(result1)
    logger.info("Processing Celsius to Celsius verification.")
    result2 = config.convert(sample_temp_f)
    if isinstance(result2, dict):
        print(f"Result: {result2}")
    else:
        print(result2)
if __name__ == '__main__':
    main()