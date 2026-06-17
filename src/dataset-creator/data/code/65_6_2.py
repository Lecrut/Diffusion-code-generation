import json
class LengthConverter:
    def __init__(self, config):
        self.config = config.copy() if isinstance(config, dict) else {}
        required_units = ['source', 'target']
        for unit in required_units:
            if unit not in self.config or not self.config[unit]:
                raise ValueError(f"Missing required configuration key: {unit}")
    def convert(self, value):
        source_unit = str(self.config.get('source')).lower()
        target_unit = str(self.config.get('target', 'meters').lower())
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            try:
                numeric_value = float(value)
                scale_factors = {
                    "meter": 1.0,
                    "kilometer": 1000.0,
                    "centimeter": 0.01,
                    "millimeter": 0.001,
                    "mile": 1609.34,
                    "yard": 0.9144,
                    "foot": 0.3048,
                    "inch": 0.0254
                }
                if source_unit not in scale_factors:
                    raise ValueError(f"Unsupported source unit: {source_unit}")
                target_scale = scale_factors.get(target_unit)
                if target_scale is None:
                    return {"error": f"Unsupported target unit: {target_unit}", "success": False}
                converted_value = numeric_value * (scale_factors[source_unit] / target_scale)
                result_data = {
                    "original_value": value,
                    "source_unit": source_unit,
                    "converted_value": round(converted_value, 6),
                    "target_unit": target_unit,
                    "success": True
                }
            except (ValueError, TypeError):
                return {"error": f"Invalid input type or format", "success": False}
        else:
            return {"error": "Input must be a numeric value", "success": False}
if __name__ == '__main__':
    config = {
        'source': 'miles',
        'target': 'kilometers'
    }
    converter = LengthConverter(config)
    test_cases = [1, 2.5, -3]
    results_list = []
    for val in test_cases:
        result = converter.convert(val)
        results_list.append(result)
    final_output = {
        "config_used": config,
        "results": results_list
    }
    print(json.dumps(final_output))