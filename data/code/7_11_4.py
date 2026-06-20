class TimeConverter:
    def __init__(self):
        self.units = {
            'nanosecond': 1e-9,
            'microsecond': 1e-6,
            'millisecond': 1e-3,
            'second': 1,
            'minute': 60,
            'hour': 3600,
            'day': 86400,
            'week': 604800,
            'month': 2629746,
            'year': 31556952
        }

    def convert(self, value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        if from_unit not in self.units:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in self.units:
            raise ValueError(f"Unknown unit: {to_unit}")
        seconds = value * self.units[from_unit]
        result = seconds / self.units[to_unit]
        return result

    def seconds_to_minutes(self, seconds):
        return self.convert(seconds, 'second', 'minute')

    def minutes_to_seconds(self, minutes):
        return self.convert(minutes, 'minute', 'second')

    def hours_to_days(self, hours):
        return self.convert(hours, 'hour', 'day')

    def days_to_hours(self, days):
        return self.convert(days, 'day', 'hour')

    def milliseconds_to_hours(self, milliseconds):
        return self.convert(milliseconds, 'millisecond', 'hour')

    def weeks_to_seconds(self, weeks):
        return self.convert(weeks, 'week', 'second')

if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.seconds_to_minutes(120))
    print(converter.minutes_to_seconds(2.5))
    print(converter.hours_to_days(24))
    print(converter.days_to_hours(1))
    print(converter.milliseconds_to_hours(3600000))
    print(converter.weeks_to_seconds(1))
    print(converter.convert(1, 'year', 'day'))
    print(converter.convert(1, 'nanosecond', 'millisecond'))