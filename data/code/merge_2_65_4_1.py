import math
class UnitConverter:
    def convert(self, value, from_unit, to_unit):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        base_meters = self._get_base_value(from_unit)
        converted_to_base = value / base_meters
        target_base = self._get_base_value(to_unit)
        return converted_to_base * target_base
    def _get_base_value(self, unit):
        bases = {
            'm': 1.0,
            'km': 1000.0,
            'cm': 0.01,
            'mm': 0.001,
            'mi': 1609.344,
            'yd': 0.9144,
            'ft': 0.3048,
            'in': 0.0254
        }
        if unit not in bases:
            raise ValueError(f"Unsupported unit: {unit}")
        return bases[unit]
def convert_batch(values, from_unit, to_unit):
    results = []
    for val in values:
        try:
            converted_val = UnitConverter().convert(val, from_unit, to_unit)
            results.append(converted_val)
        except Exception as e:
            raise RuntimeError(f"Conversion failed at index {values.index(val)}") from e
    return results
if __name__ == '__main__':
    sample_data = [10.5, 2000, 3456789]
    converted_results = convert_batch(sample_data, 'km', 'm')
    print(converted_results)