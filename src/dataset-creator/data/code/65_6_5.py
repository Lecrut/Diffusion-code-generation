import json
class LengthConverter:
    def __init__(self, config=None):
        self.config = config if config is not None else {}
    def _validate_input(self, value, unit_from, unit_to):
        preconditions = [
            isinstance(value, (int, float)),
            value >= 0,
            unit_from in ["m", "km", "cm", "mm", "nm"],
            unit_to in ["m", "km", "cm", "mm", "nm"]
        ]
        if not all(preconditions):
            raise ValueError("Invalid input: value must be non-negative, and units must be m/km/cm/mm/nm")
    def _get_scaling_factor(self, unit_from, unit_to):
        base_m = {
            "km": 10**3,
            "cm": 10**-2,
            "mm": 10**-3,
            "nm": 10**-9
        }
        factor_from = self.config.get("scale_" + unit_from) or base_m[unit_from]
        factor_to = self.config.get("scale_" + unit_to) or base_m[unit_to]
        return (factor_from / factor_to) * self.config.get("global_multiplier", 1.0)
    def convert(self, value: float | int, from_unit: str, to_unit: str):
        try:
            self._validate_input(value, from_unit, to_unit)
            result = value * self._get_scaling_factor(from_unit, to_unit)
            return {
                "original_value": value,
                "from_unit": from_unit,
                "to_unit": to_unit,
                "converted_value": round(result, 6),
                "status": "success"
            }
        except Exception as e:
            return {
                "error": str(e),
                "original_value": value if isinstance(value, (int, float)) else None,
                "from_unit": from_unit,
                "to_unit": to_unit,
                "status": "failed"
            }
if __name__ == '__main__':
    sample_config = {
        "global_multiplier": 1.0,
        "scale_km": 5 * (10**3),
        "scale_mm": 2 * (10**-3)
    }
    converter = LengthConverter(config=sample_config)
    test_cases = [
        {"value": 100, "from_unit": "km", "to_unit": "m"},
        {"value": 5.5, "from_unit": "cm", "to_unit": "mm"},
        {"value": -10, "from_unit": "m", "to_unit": "nm"}
    ]
    results = []
    for case in test_cases:
        res = converter.convert(**case)
        results.append(res)
    print(json.dumps(results))