class TimeConverter:
    def __init__(self):
        self._units = {
            'nanosecond': 1e-9,
            'microsecond': 1e-6,
            'millisecond': 1e-3,
            'second': 1,
            'minute': 60,
            'hour': 3600,
            'day': 86400,
            'week': 604800,
        }

    def convert(self, value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        if from_unit not in self._units:
            raise ValueError(f"Unsupported unit: {from_unit}")
        if to_unit not in self._units:
            raise ValueError(f"Unsupported unit: {to_unit}")
        base_value = value * self._units[from_unit]
        result = base_value / self._units[to_unit]
        return result

    def seconds_to_minutes(self, seconds):
        return self.convert(seconds, 'second', 'minute')

    def minutes_to_hours(self, minutes):
        return self.convert(minutes, 'minute', 'hour')

    def hours_to_days(self, hours):
        return self.convert(hours, 'hour', 'day')

    def days_to_weeks(self, days):
        return self.convert(days, 'day', 'week')

    def hours_to_minutes(self, hours):
        return self.convert(hours, 'hour', 'minute')

    def milliseconds_to_seconds(self, milliseconds):
        return self.convert(milliseconds, 'millisecond', 'second')

    def weeks_to_days(self, weeks):
        return self.convert(weeks, 'week', 'day')

    def days_to_hours(self, days):
        return self.convert(days, 'day', 'hour')

    def minutes_to_seconds(self, minutes):
        return self.convert(minutes, 'minute', 'second')

    def nanoseconds_to_milliseconds(self, nanoseconds):
        return self.convert(nanoseconds, 'nanosecond', 'millisecond')

    def microseconds_to_milliseconds(self, microseconds):
        return self.convert(microseconds, 'microsecond', 'millisecond')

    def seconds_to_hours(self, seconds):
        return self.convert(seconds, 'second', 'hour')

    def minutes_to_days(self, minutes):
        return self.convert(minutes, 'minute', 'day')

    def hours_to_seconds(self, hours):
        return self.convert(hours, 'hour', 'second')

    def days_to_minutes(self, days):
        return self.convert(days, 'day', 'minute')

    def weeks_to_hours(self, weeks):
        return self.convert(weeks, 'week', 'hour')

    def weeks_to_seconds(self, weeks):
        return self.convert(weeks, 'week', 'second')

    def seconds_to_weeks(self, seconds):
        return self.convert(seconds, 'second', 'week')

if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.seconds_to_minutes(120))
    print(converter.minutes_to_hours(90))
    print(converter.hours_to_days(48))
    print(converter.days_to_weeks(14))
    print(converter.hours_to_minutes(2.5))
    print(converter.milliseconds_to_seconds(1500))
    print(converter.weeks_to_days(3))
    print(converter.days_to_hours(5))
    print(converter.minutes_to_seconds(120))
    print(converter.nanoseconds_to_milliseconds(1e6))
    print(converter.microseconds_to_milliseconds(500))
    print(converter.seconds_to_hours(7200))
    print(converter.minutes_to_days(1440))
    print(converter.hours_to_seconds(1))
    print(converter.days_to_minutes(1))
    print(converter.weeks_to_hours(1))
    print(converter.weeks_to_seconds(1))
    print(converter.seconds_to_weeks(604800))
    print(converter.convert(1000, 'second', 'minute'))
    print(converter.convert(60, 'minute', 'second'))
    print(converter.convert(24, 'hour', 'day'))
    print(converter.convert(7, 'day', 'week'))
    print(converter.convert(1, 'week', 'day'))
    print(converter.convert(1, 'day', 'hour'))
    print(converter.convert(1, 'hour', 'minute'))
    print(converter.convert(1, 'minute', 'second'))
    print(converter.convert(1, 'second', 'millisecond'))
    print(converter.convert(1, 'millisecond', 'microsecond'))
    print(converter.convert(1, 'microsecond', 'nanosecond'))
    print(converter.convert(1, 'nanosecond', 'second'))
    print(converter.convert(100, 'nanosecond', 'microsecond'))
    print(converter.convert(1000, 'millisecond', 'second'))
    print(converter.convert(60, 'hour', 'minute'))
    print(converter.convert(168, 'day', 'week'))
    print(converter.convert(525600, 'year', 'hour'))