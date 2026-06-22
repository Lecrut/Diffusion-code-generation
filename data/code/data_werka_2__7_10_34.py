class TimeConverter:
    def __init__(self):
        self.time_units = {
            'second': 1,
            'minute': 60,
            'hour': 3600,
            'day': 86400,
            'week': 604800,
            'month': 2592000,
            'year': 31536000
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.time_units or to_unit not in self.time_units:
            raise ValueError("Unsupported unit. Please choose from 'second', 'minute', 'hour', 'day', 'week', 'month', 'year'.")
        value_in_seconds = value * self.time_units[from_unit]
        converted_value = value_in_seconds / self.time_units[to_unit]
        return converted_value

if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.convert(1, 'hour', 'minute'))
    print(converter.convert(24, 'day', 'hour'))
    print(converter.convert(365, 'year', 'day'))
    print(converter.convert(1000, 'second', 'week'))