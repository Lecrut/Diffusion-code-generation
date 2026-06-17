import math
class UnitConverter:
    def to_base(self, value, from_unit):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        base_factors = {
            'm': 1.0,
            'km': 1000.0,
            'cm': 0.01,
            'mm': 0.001,
            'mi': 1609.344,
            'yd': 0.9144,
            'ft': 0.3048,
            'in': 0.0254
        }
        if from_unit not in base_factors:
            raise ValueError(f"Unsupported unit: {from_unit}")
        return value * base_factors[from_unit]
def convert_batch(values, from_units):
    results = []
    for v, u in zip(values, from_units):
        try:
            converted = UnitConverter().to_base(v, u)
            results.append(converted)
        except Exception as e:
            raise RuntimeError(f"Conversion failed at index {values.index(v)}") from e
    return results
if __name__ == '__main__':
    sample_values = [100.5, 2000, -50]
    sample_units = ['m', 'km', 'cm']
    try:
        converted_data = convert_batch(sample_values, sample_units)
        print(converted_data)
    except Exception as e:
        print(f"Error occurred: {e}")