import math
class UnitConverter:
    def convert(self, value, from_unit, to_unit):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        base_units = {
            'm': 1.0,
            'km': 1000.0,
            'cm': 0.01,
            'mm': 0.001,
            'mi': 1609.344,
            'yd': 0.9144,
            'ft': 0.3048,
            'in': 0.0254
        }
        if from_unit not in base_units:
            raise ValueError(f"Invalid source unit: {from_unit}")
        if to_unit not in base_units:
            raise ValueError(f"Invalid target unit: {to_unit}")
        factor = (base_units[from_unit] / base_units[to_unit])
        return value * factor
def convert_batch(values, from_unit, to_unit):
    try:
        converter = UnitConverter()
        results = [converter.convert(v, from_unit, to_unit) for v in values]
        return results
    except (TypeError, ValueError) as e:
        raise RuntimeError(f"Conversion failed: {e}")
if __name__ == '__main__':
    sample_data = [10.5, 2000, 3600, -50]
    converted_values = convert_batch(sample_data, 'km', 'm')
    print(converted_values)