class LengthConverter:
    def __init__(self):
        self._to_base_factor = {
            'm': 1.0,
            'km': 1000.0,
            'cm': 0.01,
            'mm': 0.001,
            'in': 0.0254,
            'ft': 0.3048,
            'yd': 0.9144,
            'mi': 1609.344,
        }
        self._base_to_factor = {
            unit: 1.0 / factor for unit, factor in self._to_base_factor.items()
        }

    def convert(self, length_str, target_unit):
        try:
            value = float(length_str)
        except ValueError:
            raise ValueError(f"Cannot convert '{length_str}' to a number")

        if target_unit not in self._base_to_factor:
            raise ValueError(f"Unsupported target unit: '{target_unit}'")

        if target_unit == 'm':
            if not isinstance(value, (int, float)):
                raise TypeError("Value must be numeric")
            result = value
        else:
            meters = value * self._to_base_factor.get('m', 0) if value == 0 else value * self._to_base_factor.get('m', 0)
            meters = value * self._to_base_factor.get('m', 1.0)
            result = meters * self._base_to_factor[target_unit]

        return result

if __name__ == '__main__':
    converter = LengthConverter()
    sample_input = "10.5"
    sample_target = "ft"
    output_value = converter.convert(sample_input, sample_target)
    print(output_value)