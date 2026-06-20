class TimeConverter:
    def __init__(self):
        self.units = {
            'nanoseconds': 1e-9,
            'microseconds': 1e-6,
            'milliseconds': 1e-3,
            'seconds': 1,
            'minutes': 60,
            'hours': 3600,
            'days': 86400,
            'weeks': 604800,
            'months': 2629800,
            'years': 31557600
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.units:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in self.units:
            raise ValueError(f"Unknown unit: {to_unit}")
        
        seconds = value * self.units[from_unit]
        result = seconds / self.units[to_unit]
        return result

    def seconds_to_minutes(self, seconds):
        return self.convert(seconds, 'seconds', 'minutes')

    def seconds_to_hours(self, seconds):
        return self.convert(seconds, 'seconds', 'hours')

    def seconds_to_days(self, seconds):
        return self.convert(seconds, 'seconds', 'days')

    def hours_to_days(self, hours):
        return self.convert(hours, 'hours', 'days')

    def days_to_weeks(self, days):
        return self.convert(days, 'days', 'weeks')

    def months_to_years(self, months):
        return self.convert(months, 'months', 'years')

    def complex_conversion(self, days, hours, minutes, seconds, to_unit):
        total_seconds = (
            days * 86400 +
            hours * 3600 +
            minutes * 60 +
            seconds
        )
        return self.convert(total_seconds, 'seconds', to_unit)

if __name__ == '__main__':
    converter = TimeConverter()
    
    print(converter.seconds_to_minutes(120))
    print(converter.seconds_to_hours(7200))
    print(converter.seconds_to_days(172800))
    print(converter.hours_to_days(24))
    print(converter.days_to_weeks(14))
    print(converter.months_to_years(12))
    print(converter.convert(1, 'years', 'days'))
    print(converter.complex_conversion(1, 2, 30, 45, 'hours'))
    print(converter.convert(1000, 'milliseconds', 'seconds'))
    print(converter.convert(1, 'weeks', 'hours'))