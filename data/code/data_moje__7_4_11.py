class TimeUnitConverter:
    def __init__(self):
        self.seconds_per_minute = 60
        self.minutes_per_hour = 60
        self.hours_per_day = 24
        self.days_per_month = 30.4375
        self.months_per_year = 12

    def convert(self, value, from_unit, to_unit):
        seconds = self.to_seconds(value, from_unit)
        return self.from_seconds(seconds, to_unit)

    def to_seconds(self, value, unit):
        if unit == 'seconds':
            return value
        elif unit == 'minutes':
            return value * self.seconds_per_minute
        elif unit == 'hours':
            return value * self.minutes_per_hour * self.seconds_per_minute
        elif unit == 'days':
            return value * self.hours_per_day * self.minutes_per_hour * self.seconds_per_minute
        elif unit == 'months':
            return value * self.days_per_month * self.hours_per_day * self.minutes_per_hour * self.seconds_per_minute
        elif unit == 'years':
            return value * self.months_per_year * self.days_per_month * self.hours_per_day * self.minutes_per_hour * self.seconds_per_minute
        else:
            raise ValueError(f"Unsupported unit: {unit}")

    def from_seconds(self, seconds, unit):
        if unit == 'seconds':
            return seconds
        elif unit == 'minutes':
            return seconds / self.seconds_per_minute
        elif unit == 'hours':
            return seconds / (self.minutes_per_hour * self.seconds_per_minute)
        elif unit == 'days':
            return seconds / (self.hours_per_day * self.minutes_per_hour * self.seconds_per_minute)
        elif unit == 'months':
            return seconds / (self.days_per_month * self.hours_per_day * self.minutes_per_hour * self.seconds_per_minute)
        elif unit == 'years':
            return seconds / (self.months_per_year * self.days_per_month * self.hours_per_day * self.minutes_per_hour * self.seconds_per_minute)
        else:
            raise ValueError(f"Unsupported unit: {unit}")

    def convert_year_to_month(self, years):
        return self.convert(years, 'years', 'months')

    def convert_month_to_year(self, months):
        return self.convert(months, 'months', 'years')

    def convert_day_to_hour(self, days):
        return self.convert(days, 'days', 'hours')

    def convert_hour_to_day(self, hours):
        return self.convert(hours, 'hours', 'days')

    def convert_minute_to_second(self, minutes):
        return self.convert(minutes, 'minutes', 'seconds')

    def convert_second_to_minute(self, seconds):
        return self.convert(seconds, 'seconds', 'minutes')

    def convert_year_to_day(self, years):
        return self.convert(years, 'years', 'days')

    def convert_day_to_year(self, days):
        return self.convert(days, 'days', 'years')

    def convert_hour_to_second(self, hours):
        return self.convert(hours, 'hours', 'seconds')

    def convert_second_to_hour(self, seconds):
        return self.convert(seconds, 'seconds', 'hours')

if __name__ == '__main__':
    converter = TimeUnitConverter()
    print(converter.convert(1, 'years', 'months'))
    print(converter.convert(12, 'months', 'years'))
    print(converter.convert(1, 'days', 'hours'))
    print(converter.convert(24, 'hours', 'days'))
    print(converter.convert(1, 'minutes', 'seconds'))
    print(converter.convert(60, 'seconds', 'minutes'))
    print(converter.convert(1, 'years', 'days'))
    print(converter.convert(365.25, 'days', 'years'))
    print(converter.convert(1, 'hours', 'seconds'))
    print(converter.convert(3600, 'seconds', 'hours'))
    print(converter.convert(365.25, 'days', 'seconds'))
    print(converter.convert(31557600, 'seconds', 'years'))