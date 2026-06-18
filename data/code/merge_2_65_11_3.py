from dataclasses import dataclass
@dataclass(frozen=True)
class LengthConverter:
    def convert(self, value_str: str) -> dict[str, float]:
        try:
            numeric_value = float(value_str.strip())
        except ValueError:
            raise ValueError("Input must be a valid number.")
        units = {
            "meters": numeric_value,
            "kilometers": numeric_value / 1000.0,
            "centimeters": numeric_value * 100.0,
            "millimeters": numeric_value * 1000.0,
            "inches": numeric_value * 39.3701,
            "feet": numeric_value / 2.54,
        }
        return units
if __name__ == '__main__':
    converter = LengthConverter()
    sample_input = "1"
    result = converter.convert(sample_input)
    print(result)