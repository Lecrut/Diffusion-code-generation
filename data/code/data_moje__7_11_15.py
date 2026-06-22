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
            'month': 2629800,
            'year': 31557600
        }

    def convert(self, value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        if from_unit not in self._units:
            raise ValueError(f"Unknown source unit: {from_unit}")
        if to_unit not in self._units:
            raise ValueError(f"Unknown target unit: {to_unit}")
        value_in_seconds = value * self._units[from_unit]
        result = value_in_seconds / self._units[to_unit]
        return result

    def seconds_to_minutes(self, seconds):
        return self.convert(seconds, 'second', 'minute')

    def seconds_to_hours(self, seconds):
        return self.convert(seconds, 'second', 'hour')

    def seconds_to_days(self, seconds):
        return self.convert(seconds, 'second', 'day')

    def minutes_to_seconds(self, minutes):
        return self.convert(minutes, 'minute', 'second')

    def minutes_to_hours(self, minutes):
        return self.convert(minutes, 'minute', 'hour')

    def hours_to_seconds(self, hours):
        return self.convert(hours, 'hour', 'second')

    def hours_to_minutes(self, hours):
        return self.convert(hours, 'hour', 'minute')

    def hours_to_days(self, hours):
        return self.convert(hours, 'hour', 'day')

    def days_to_seconds(self, days):
        return self.convert(days, 'day', 'second')

    def days_to_hours(self, days):
        return self.convert(days, 'day', 'hour')

    def days_to_minutes(self, days):
        return self.convert(days, 'day', 'minute')

    def days_to_weeks(self, days):
        return self.convert(days, 'day', 'week')

    def weeks_to_days(self, weeks):
        return self.convert(weeks, 'week', 'day')

    def weeks_to_hours(self, weeks):
        return self.convert(weeks, 'week', 'hour')

    def weeks_to_minutes(self, weeks):
        return self.convert(weeks, 'week', 'minute')

    def weeks_to_seconds(self, weeks):
        return self.convert(weeks, 'week', 'second')

    def months_to_days(self, months):
        return self.convert(months, 'month', 'day')

    def months_to_hours(self, months):
        return self.convert(months, 'month', 'hour')

    def months_to_minutes(self, months):
        return self.convert(months, 'month', 'minute')

    def months_to_seconds(self, months):
        return self.convert(months, 'month', 'second')

    def years_to_days(self, years):
        return self.convert(years, 'year', 'day')

    def years_to_hours(self, years):
        return self.convert(years, 'year', 'hour')

    def years_to_minutes(self, years):
        return self.convert(years, 'year', 'minute')

    def years_to_seconds(self, years):
        return self.convert(years, 'year', 'second')

    def milliseconds_to_seconds(self, milliseconds):
        return self.convert(milliseconds, 'millisecond', 'second')

    def milliseconds_to_minutes(self, milliseconds):
        return self.convert(milliseconds, 'millisecond', 'minute')

    def microseconds_to_seconds(self, microseconds):
        return self.convert(microseconds, 'microsecond', 'second')

    def microseconds_to_minutes(self, microseconds):
        return self.convert(microseconds, 'microsecond', 'minute')

    def nanoseconds_to_seconds(self, nanoseconds):
        return self.convert(nanoseconds, 'nanosecond', 'second')

    def nanoseconds_to_minutes(self, nanoseconds):
        return self.convert(nanoseconds, 'nanosecond', 'minute')

if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.seconds_to_minutes(120))
    print(converter.seconds_to_hours(3600))
    print(converter.seconds_to_days(86400))
    print(converter.minutes_to_hours(60))
    print(converter.hours_to_days(24))
    print(converter.days_to_weeks(7))
    print(converter.weeks_to_days(1))
    print(converter.convert(1, 'year', 'day'))
    print(converter.convert(1, 'month', 'day'))
    print(converter.milliseconds_to_seconds(1000))
    print(converter.microseconds_to_seconds(1000000))
    print(converter.nanoseconds_to_seconds(1000000000))
    print(converter.convert(1.5, 'hour', 'minute'))
    print(converter.convert(0.5, 'day', 'hour'))
    print(converter.convert(2.5, 'week', 'day'))
    print(converter.convert(0.25, 'year', 'month'))