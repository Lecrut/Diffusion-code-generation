import math
class UnitConverter:
    def convert(self, value, from_unit, to_unit):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number.")
        valid_units = ['m', 'km', 'cm', 'mm', 'mi']
        if from_unit not in valid_units or to_unit not in valid_units:
            raise ValueError(f"Invalid units. Must use one of {valid_units}.")
        base_meters = self._get_base_from(from_unit, value)
        return round(base_meters * self._get_factor(to_unit), 6)
    def _get_base_from(self, unit, val):
        if unit == 'm':
            return val
        elif unit == 'km':
            return val * 1000.0
        elif unit == 'cm':
            return val / 100.0
        elif unit == 'mm':
            return val / 1000.0
        elif unit == 'mi':
            return val * 1609.344
    def _get_factor(self, unit):
        if unit == 'm':
            return 1.0
        elif unit == 'km':
            return 0.001
        elif unit == 'cm':
            return 0.01
        elif unit == 'mm':
            return 0.001
        elif unit == 'mi':
            return 0.000621371
class BatchConverter:
    def __init__(self):
        self.converter = UnitConverter()
    def convert_batch(self, values, from_unit, to_unit):
        try:
            results = [self.converter.convert(v, from_unit, to_unit) for v in values]
            return list(results), None
        except Exception as e:
            return [], str(e)
if __name__ == '__main__':
    data = [[100.5, 2500, -5], [3.7, 4828.032, 6]]
    batch_processor = BatchConverter()
    for i in range(len(data)):
        values = data[i]
        converted_values, error = batch_processor.convert_batch(values, 'm', 'km')
        if not isinstance(error, str):
            print(f"Error occurred: {error}")
        else:
            output_list = [f"{v:.6}" for v in converted_values]
            print(f"Input Batch {i}: {values} -> Output: {[float(x) for x in output_list]}")