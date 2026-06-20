import math

class TimeConverter:
    def __init__(self, value, unit):
        valid_units = ['seconds', 'minutes', 'hours', 'days']
        if unit not in valid_units:
            raise ValueError(f"Invalid unit '{unit}'. Must be one of {valid_units}")
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        if value < 0:
            raise ValueError("Value cannot be negative")
        self.value = float(value)
        self.unit = unit.lower()
        self._to_seconds = {
            'seconds': 1,
            'minutes': 60,
            'hours': 3600,
            'days': 86400
        }

    def get_seconds(self):
        return self.value * self._to_seconds[self.unit]

    def convert_to(self, target_unit):
        valid_units = ['seconds', 'minutes', 'hours', 'days']
        if target_unit not in valid_units:
            raise ValueError(f"Invalid target unit '{target_unit}'. Must be one of {valid_units}")
        total_seconds = self.get_seconds()
        factor = self._to_seconds[target_unit]
        return total_seconds / factor

    def convert_all(self):
        units = ['seconds', 'minutes', 'hours', 'days']
        results = {}
        total_seconds = self.get_seconds()
        for u in units:
            factor = self._to_seconds[u]
            results[u] = total_seconds / factor
        return results

if __name__ == '__main__':
    converter = TimeConverter(2.5, 'hours')
    print(converter.convert_to('minutes'))
    all_results = converter.convert_all()
    for unit, value in all_results.items():
        print(f"{unit}: {value}")