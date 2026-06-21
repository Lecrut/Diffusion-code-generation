class TimeConverter:
    def __init__(self, duration, unit):
        self.duration = duration
        self.unit = unit
        self._validate_input()
        self.total_seconds = self._to_seconds()

    def _validate_input(self):
        if not isinstance(self.duration, (int, float)):
            raise ValueError("Duration must be a number.")
        if self.duration < 0:
            raise ValueError("Duration cannot be negative.")
        supported_units = {'seconds', 'minutes', 'hours', 'days'}
        if self.unit not in supported_units:
            raise ValueError(f"Unsupported unit: {self.unit}")

    def _to_seconds(self):
        conversion_factors = {
            'seconds': 1,
            'minutes': 60,
            'hours': 3600,
            'days': 86400
        }
        return self.duration * conversion_factors[self.unit]

    def convert_to_units(self):
        return {
            'seconds': self.total_seconds,
            'minutes': self.total_seconds / 60,
            'hours': self.total_seconds / 3600,
            'days': self.total_seconds / 86400
        }

if __name__ == '__main__':
    converter = TimeConverter(1, 'hour')
    print(converter.convert_to_units())