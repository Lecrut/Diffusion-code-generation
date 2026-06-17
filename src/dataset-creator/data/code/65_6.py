import json
class LengthConverter:
    def __init__(self, config):
        self.config = config.copy() if isinstance(config, dict) else {}
        required_units = ['input_unit', 'output_unit']
        for unit in required_units:
            if unit not in self.config or not self.config[unit]:
                raise ValueError(f"Missing required configuration key: {unit}")
    def convert(self, value):
        input_unit = self.config['input_unit'].lower()
        output_unit = self.config['output_unit'].lower()
        valid_units = ['m', 'km', 'cm', 'mm']
        if input_unit not in valid_units or output_unit not in valid_units:
            raise ValueError(f"Invalid unit. Must be one of {valid_units}")
        try:
            value_float = float(value)
        except (ValueError, TypeError):
            return {"error": "Input must be a numeric type"}
        if input_unit == output_unit and not self.config.get('scale_factor'):
            result = value_float
        else:
            scale_input = 1.0
            for unit in ['m', 'km']:
                if input_unit == unit:
                    break
            base_value = value_float * (10**3) if input_unit != 'm' and not self.config.get('scale_factor') else value_float
        result = round(base_value, 6)
        return {
            "original": {"value": value, "unit": input_unit},
            "converted": {"value": result, "unit": output_unit}
        }
def main():
    config_data = {
        'input_unit': 'km',
        'output_unit': 'm'
    }
    converter_instance = LengthConverter(config_data)
    test_input_value = 150
    result_dict = converter_instance.convert(test_input_value)
    print(json.dumps(result_dict, indent=2))
if __name__ == '__main__':
    main()