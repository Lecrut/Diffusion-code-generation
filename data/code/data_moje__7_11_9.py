from decimal import Decimal, getcontext, InvalidOperation

getcontext().prec = 50

class TimeConverter:
    def __init__(self):
        self.units = {
            'nanosecond': Decimal('1e-9'),
            'microsecond': Decimal('1e-6'),
            'millisecond': Decimal('1e-3'),
            'second': Decimal(1),
            'minute': Decimal(60),
            'hour': Decimal(3600),
            'day': Decimal(86400),
            'week': Decimal(604800),
            'year': Decimal(31557600),
            'decade': Decimal(315576000),
            'century': Decimal(3155760000),
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.units:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in self.units:
            raise ValueError(f"Unknown unit: {to_unit}")
        
        try:
            decimal_value = Decimal(str(value))
        except (InvalidOperation, ValueError, TypeError):
            raise ValueError(f"Invalid value: {value}")
        
        if decimal_value < 0:
            raise ValueError("Time value cannot be negative")
        
        from_factor = self.units[from_unit]
        to_factor = self.units[to_unit]
        
        seconds = decimal_value * from_factor
        result = seconds / to_factor
        
        return result

    def seconds_to_minutes(self, seconds):
        return self.convert(seconds, 'second', 'minute')

    def minutes_to_hours(self, minutes):
        return self.convert(minutes, 'minute', 'hour')

    def hours_to_days(self, hours):
        return self.convert(hours, 'hour', 'day')

    def days_to_weeks(self, days):
        return self.convert(days, 'day', 'week')

    def weeks_to_years(self, weeks):
        return self.convert(weeks, 'week', 'year')

    def years_to_days(self, years):
        return self.convert(years, 'year', 'day')

    def milliseconds_to_seconds(self, milliseconds):
        return self.convert(milliseconds, 'millisecond', 'second')

    def microseconds_to_milliseconds(self, microseconds):
        return self.convert(microseconds, 'microsecond', 'millisecond')

    def nanoseconds_to_microseconds(self, nanoseconds):
        return self.convert(nanoseconds, 'nanosecond', 'microsecond')

if __name__ == '__main__':
    converter = TimeConverter()
    
    print(converter.seconds_to_minutes(120))
    print(converter.minutes_to_hours(90))
    print(converter.hours_to_days(24))
    print(converter.days_to_weeks(14))
    print(converter.weeks_to_years(52))
    print(converter.years_to_days(1))
    print(converter.milliseconds_to_seconds(1500))
    print(converter.microseconds_to_milliseconds(1000))
    print(converter.nanoseconds_to_microseconds(1000))
    print(converter.convert(1, 'day', 'nanosecond'))
    print(converter.convert(86400, 'second', 'day'))
    print(converter.convert(0, 'hour', 'minute'))
    print(converter.convert(3.5, 'hour', 'minute'))
    print(converter.convert(1.5, 'day', 'hour'))