class TimeConverter:
    def __init__(self):
        self._units = {
            'nanosecond': 1e-9,
            'microsecond': 1e-6,
            'millisecond': 1e-3,
            'second': 1.0,
            'minute': 60.0,
            'hour': 3600.0,
            'day': 86400.0,
            'week': 604800.0,
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self._units:
            raise ValueError(f"Unsupported unit: {from_unit}")
        if to_unit not in self._units:
            raise ValueError(f"Unsupported unit: {to_unit}")

        from_seconds = value * self._units[from_unit]
        to_value = from_seconds / self._units[to_unit]
        return to_value

    def seconds_to_minutes(self, seconds):
        return self.convert(seconds, 'second', 'minute')

    def seconds_to_hours(self, seconds):
        return self.convert(seconds, 'second', 'hour')

    def seconds_to_days(self, seconds):
        return self.convert(seconds, 'second', 'day')

    def minutes_to_seconds(self, minutes):
        return self.convert(minutes, 'minute', 'second')

    def hours_to_seconds(self, hours):
        return self.convert(hours, 'hour', 'second')

    def days_to_seconds(self, days):
        return self.convert(days, 'day', 'second')

    def hours_to_minutes(self, hours):
        return self.convert(hours, 'hour', 'minute')

    def days_to_hours(self, days):
        return self.convert(days, 'day', 'hour')

if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.seconds_to_minutes(125))
    print(converter.seconds_to_hours(7200))
    print(converter.seconds_to_days(86400))
    print(converter.minutes_to_seconds(5))
    print(converter.hours_to_seconds(3))
    print(converter.days_to_seconds(2))
    print(converter.hours_to_minutes(2.5))
    print(converter.days_to_hours(3.5))
    print(converter.convert(1000, 'millisecond', 'second'))
    print(converter.convert(1, 'day', 'hour'))