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
        if from_unit not in self.units:
            raise ValueError(f"Invalid source unit: {from_unit}")
        if to_unit not in self.units:
            raise ValueError(f"Invalid target unit: {to_unit}")
        
        seconds = value * self.units[from_unit]
        result = seconds / self.units[to_unit]
        return result

    def seconds_to_minutes(self, seconds):
        return self.convert(seconds, 'second', 'minute')

    def seconds_to_hours(self, seconds):
        return self.convert(seconds, 'second', 'hour')

    def seconds_to_days(self, seconds):
        return self.convert(seconds, 'second', 'day')

    def minutes_to_hours(self, minutes):
        return self.convert(minutes, 'minute', 'hour')

    def minutes_to_days(self, minutes):
        return self.convert(minutes, 'minute', 'day')

    def hours_to_days(self, hours):
        return self.convert(hours, 'hour', 'day')

    def hours_to_weeks(self, hours):
        return self.convert(hours, 'hour', 'week')

    def days_to_weeks(self, days):
        return self.convert(days, 'day', 'week')

    def days_to_years(self, days):
        return self.convert(days, 'day', 'year')

    def milliseconds_to_seconds(self, milliseconds):
        return self.convert(milliseconds, 'millisecond', 'second')

    def microseconds_to_milliseconds(self, microseconds):
        return self.convert(microseconds, 'microsecond', 'millisecond')

    def nanoseconds_to_microseconds(self, nanoseconds):
        return self.convert(nanoseconds, 'nanosecond', 'microsecond')

if __name__ == '__main__':
    converter = TimeConverter()
    
    print(converter.seconds_to_minutes(120))
    print(converter.seconds_to_hours(3600))
    print(converter.seconds_to_days(86400))
    print(converter.minutes_to_hours(120))
    print(converter.minutes_to_days(1440))
    print(converter.hours_to_days(24))
    print(converter.hours_to_weeks(168))
    print(converter.days_to_weeks(7))
    print(converter.days_to_years(365.25))
    print(converter.milliseconds_to_seconds(1000))
    print(converter.microseconds_to_milliseconds(1000))
    print(converter.nanoseconds_to_microseconds(1000))
    print(converter.convert(1, 'year', 'day'))
    print(converter.convert(1, 'week', 'hour'))
    print(converter.convert(45.5, 'minute', 'second'))
    print(converter.convert(2.5, 'hour', 'minute'))
    print(converter.convert(100, 'millisecond', 'nanosecond'))