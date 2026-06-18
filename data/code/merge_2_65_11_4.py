from dataclasses import dataclass
@dataclass(frozen=True)
class UnitConverter:
    def convert(self, value_str: str) -> dict[str, float]:
        try:
            numeric_value = float(value_str.strip())
        except ValueError:
            return {}
        units = {
            "m": 1.0,
            "km": 1_000.0,
            "cm": 0.01,
            "mm": 0.001,
            "us": 1e-6,
            "ms": 1e-3,
            "s": 1.0,
            "h": 3_600.0,
            "d": 86_400.0,
        }
        result = {}
        for unit_name, factor in units.items():
            try:
                converted_value = numeric_value * factor if isinstance(factor, float) else numeric_value / factor
                key = f"{unit_name} {numeric_value:.2f}"
                result[key] = round(converted_value, 6)
            except (TypeError, OverflowError):
                continue
        return result
if __name__ == '__main__':
    converter = UnitConverter()
    test_inputs = ["5", "10.5 km", "-3 us"]
    for input_str in test_inputs:
        print(f"Input: {input_str} -> Output: {converter.convert(input_str)}")