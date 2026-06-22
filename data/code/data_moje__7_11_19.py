class TimeConverter:
    UNITS = {
        'nanoseconds': 1e-9,
        'microseconds': 1e-6,
        'milliseconds': 1e-3,
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400,
        'weeks': 604800,
    }

    def __init__(self):
        self._unit_map = self.UNITS

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self._unit_map:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in self._unit_map:
            raise ValueError(f"Unknown unit: {to_unit}")
        from_seconds = value * self._unit_map[from_unit]
        to_value = from_seconds / self._unit_map[to_unit]
        return to_value

    def seconds_to_minutes(self, seconds):
        return self.convert(seconds, 'seconds', 'minutes')

    def minutes_to_hours(self, minutes):
        return self.convert(minutes, 'minutes', 'hours')

    def hours_to_days(self, hours):
        return self.convert(hours, 'hours', 'days')

    def days_to_weeks(self, days):
        return self.convert(days, 'days', 'weeks')

    def nanoseconds_to_seconds(self, nanoseconds):
        return self.convert(nanoseconds, 'nanoseconds', 'seconds')

    def milliseconds_to_minutes(self, milliseconds):
        return self.convert(milliseconds, 'milliseconds', 'minutes')

if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.seconds_to_minutes(120))
    print(converter.minutes_to_hours(90))
    print(converter.hours_to_days(24))
    print(converter.days_to_weeks(14))
    print(converter.nanoseconds_to_seconds(1000000000))
    print(converter.milliseconds_to_minutes(60000))
    print(converter.convert(1, 'days', 'seconds'))
    print(converter.convert(100, 'hours', 'minutes'))