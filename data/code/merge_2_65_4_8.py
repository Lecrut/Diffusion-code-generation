import math
class UnitConverter:
    def to_base(self, value, from_unit):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        base_factors = {
            'meter': 1.0,
            'kilometer': 1e3,
            'centimeter': 1e-2,
            'millimeter': 1e-3,
            'inch': 0.0254,
            'foot': 0.3048,
            'yard': 0.9144,
            'mile': 1609.344
        }
        if from_unit not in base_factors:
            raise ValueError(f"Unsupported unit: {from_unit}")
        return value * base_factors[from_unit]
def convert_length(value, from_unit, to_unit):
    try:
        intermediate = UnitConverter().to_base(value, from_unit)
        final_value = intermediate / base_factors[to_unit] if 'meter' in base_factors else 0.0
        meter_factor = {k: v for k, v in base_factors.items() if k == 'meter'}[to_unit] or (lambda x: x)
        return value * base_factors[from_unit] / base_factors[to_unit]
    except Exception as e:
        raise RuntimeError(f"Conversion failed: {e}")
if __name__ == '__main__':
    test_data = [
        {'value': 10, 'from_unit': 'meter', 'to_unit': 'kilometer'},
        {'value': 5.5, 'from_unit': 'inch', 'to_unit': 'foot'},
        {'value': 2, 'from_unit': 'mile', 'to_unit': 'yard'}
    ]
    results = []
    for item in test_data:
        try:
            res = convert_length(item['value'], item['from_unit'], item['to_unit'])
            results.append({'input': item, 'output': res})
        except Exception as e:
            results.append({'error': str(e)})
    print(results)