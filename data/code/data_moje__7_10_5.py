import sys

class TimeConverter:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
        self.units = ['seconds', 'minutes', 'hours', 'days']
        self.convert_to_seconds_map = {
            'seconds': 1,
            'minutes': 60,
            'hours': 3600,
            'days': 86400
        }

    def _validate(self):
        if not isinstance(self.value, (int, float)):
            raise ValueError("Value must be a number")
        if self.value < 0:
            raise ValueError("Value must be non-negative")
        if self.unit not in self.units:
            raise ValueError(f"Unit must be one of {self.units}")

    def convert(self):
        self._validate()
        seconds = self.value * self.convert_to_seconds_map[self.unit]
        result = {}
        for unit_name, factor in self.convert_to_seconds_map.items():
            result[unit_name] = seconds / factor
        return result

def main():
    sample_value = 2.5
    sample_unit = 'hours'
    converter = TimeConverter(sample_value, sample_unit)
    converted_values = converter.convert()
    print(converted_values)

if __name__ == '__main__':
    main()