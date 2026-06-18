import json
class LengthConverter:
    def __init__(self, config=None):
        self.config = config if config is not None else {}
    def _validate_input(self, value, unit_in, unit_out):
        preconditions = [
            isinstance(value, (int, float)),
            value >= 0,
            unit_in in ["m", "km", "cm", "mm", "in", "ft"],
            unit_out in ["m", "km", "cm", "mm", "in", "ft"]
        ]
        if not all(preconditions):
            raise ValueError("Invalid input: value must be non-negative, and units must be one of ['m', 'km', 'cm', 'mm', 'in', 'ft'].")
    def _get_scaling_factor(self, unit_in, unit_out):
        base_meters = {
            "m": 1.0,
            "km": 1000.0,
            "cm": 0.01,
            "mm": 0.001,
            "in": 0.0254,
            "ft": 0.3048
        }
        if unit_in not in base_meters or unit_out not in base_meters:
            return None
        factor = self.config.get(f"{unit_in}_{unit_out}", 
                                (base_meters[unit_in] / base_meters[unit_out]))
        custom_factor = self.config.get("custom_scaling", {})
        if isinstance(custom_factor, dict) and unit_in in custom_factor:
            return custom_factor[unit_in].get(unit_out, factor)
        return factor
    def convert(self, value, from_unit, to_unit):
        try:
            self._validate_input(value, from_unit, to_unit)
            if not isinstance(from_unit, str) or not isinstance(to_unit, str):
                raise ValueError("Units must be strings.")
            scaling_factor = self._get_scaling_factor(from_unit, to_unit)
            result = value * scaling_factor
            return {
                "original_value": float(value),
                "from_unit": from_unit.lower(),
                "to_unit": to_unit.lower(),
                "converted_value": round(result, 6),
                "status": "success"
            }
        except Exception as e:
            error_message = str(e) if isinstance(e, ValueError) else f"{type(e).__name__}: {str(e)}"
            return {
                "original_value": None,
                "from_unit": from_unit.lower(),
                "to_unit": to_unit.lower(),
                "converted_value": None,
                "status": "error",
                "message": error_message
            }
if __name__ == '__main__':
    sample_config = {
        "custom_scaling": {
            "km": {"m": 1000.5}
        }
    }
    converter_instance = LengthConverter(config=sample_config)
    test_cases = [
        (1, "ft", "in"),
        (2738469, "mm", "cm"),
        (-5, "m", "km")
    ]
    results = []
    for value, from_unit, to_unit in test_cases:
        result_data = converter_instance.convert(value, from_unit, to_unit)
        json_output = json.dumps(result_data, ensure_ascii=False)
        results.append(json_output)
    print("\n".join(results))