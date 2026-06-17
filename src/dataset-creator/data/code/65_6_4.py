import json
class UnitConverter:
    def __init__(self, config=None):
        self.config = config if config else {}
    def _validate_input(self, value, unit):
        preconditions = [isinstance(value, (int, float)), isinstance(unit, str)]
        for condition in preconditions:
            if not condition:
                raise ValueError("Invalid input type or unit string")
    def convert_length(self, length_value, from_unit, to_unit):
        self._validate_input(length_value, from_unit)
        base_factors = {
            'm': 1.0,
            'km': 1e3,
            'cm': 1e-2,
            'mm': 1e-3,
            'in': 0.0254,
            'ft': 0.0254 * 3.28084,
            'yd': 0.09144,
        }
        if from_unit not in base_factors or to_unit not in base_factors:
            raise ValueError(f"Unsupported units: {from_unit}, {to_unit}")
        factor_from = self.config.get('scale_' + from_unit.lower(), base_factors[from_unit])
        factor_to = self.config.get('scale_' + to_unit.lower(), base_factors[to_unit])
        converted_value = length_value * (factor_from / factor_to)
        return {
            'original_length': length_value,
            'from_unit': from_unit,
            'to_unit': to_unit,
            'converted_value': float(converted_value),
            'status': "success"
        }
if __name__ == '__main__':
    sample_config = {
        'scale_m': 1.0,
        'scale_km': 2e3,
        'scale_in': 0.05,
    }
    converter = UnitConverter(config=sample_config)
    test_data = [
        {'length_value': 100, 'from_unit': 'm', 'to_unit': 'km'},
        {'length_value': 3600, 'from_unit': 's', 'to_unit': 'ms'}                                                                                                                                                                                    
    ]
    result = converter.convert_length(100, 'm', 'km')
    print(json.dumps(result))