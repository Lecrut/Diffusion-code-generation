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
        factor = base_units[from_unit] / base_units[to_unit]
        return value * factor
def batch_convert(values, from_unit, to_unit):
    try:
        results = [UnitConverter().convert(v, from_unit, to_unit) for v in values]
        return results
    except Exception as e:
        raise RuntimeError(f"Conversion failed: {e}")
if __name__ == '__main__':
    sample_data = [10.5, 200, -50.3, 1609.344]
    try:
        converted_meters = batch_convert(sample_data, 'km', 'm')
        print("Input (km):", sample_data)
        print("Output (m):", converted_meters)
        inch_to_feet = batch_convert([12.0, 36.0], 'in', 'ft')
        print("\nInput (in): [12.0, 36.0]")
        print("Output (ft):", inch_to_feet)
    except Exception as error:
        print(f"Error occurred during batch conversion:", str(error))