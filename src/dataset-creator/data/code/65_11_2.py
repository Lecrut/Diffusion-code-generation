from dataclasses import dataclass
@dataclass(frozen=True)
class LengthConverter:
    def convert(self, value_str: str):
        try:
            numeric_value = float(value_str.strip())
            if not (numeric_value > 0 and isinstance(numeric_value, (int, float))):
                raise ValueError("Input must be a positive number.")
            return {
                "meters": numeric_value / 1_000_000,
                "kilometers": numeric_value * 2.54e-7,
                "centimeters": numeric_value * 100,
                "millimeters": numeric_value * 1_000_000,
            }
        except ValueError:
            return {"error": f"Invalid input '{value_str}'. Please provide a valid positive number."}
if __name__ == '__main__':
    converter = LengthConverter()
    sample_inputs = ["1", "2.5", "invalid"]
    for inp in sample_inputs:
        print(converter.convert(inp))