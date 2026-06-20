class TimeUnitConverter:
    SECONDS_PER_MINUTE = 60
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_DAY = 86400
    DAYS_PER_MONTH = 30.4375
    DAYS_PER_YEAR = 365.25
    SECONDS_PER_MONTH = SECONDS_PER_DAY * DAYS_PER_MONTH
    SECONDS_PER_YEAR = SECONDS_PER_DAY * DAYS_PER_YEAR

    def to_seconds(self, value, unit):
        unit = unit.lower()
        if unit == 'second' or unit == 'seconds':
            return value
        elif unit == 'minute' or unit == 'minutes':
            return value * self.SECONDS_PER_MINUTE
        elif unit == 'hour' or unit == 'hours':
            return value * self.SECONDS_PER_HOUR
        elif unit == 'day' or unit == 'days':
            return value * self.SECONDS_PER_DAY
        elif unit == 'month' or unit == 'months':
            return value * self.SECONDS_PER_MONTH
        elif unit == 'year' or unit == 'years':
            return value * self.SECONDS_PER_YEAR
        else:
            raise ValueError(f"Unknown time unit: {unit}")

    def from_seconds(self, seconds, unit):
        unit = unit.lower()
        if unit == 'second' or unit == 'seconds':
            return seconds
        elif unit == 'minute' or unit == 'minutes':
            return seconds / self.SECONDS_PER_MINUTE
        elif unit == 'hour' or unit == 'hours':
            return seconds / self.SECONDS_PER_HOUR
        elif unit == 'day' or unit == 'days':
            return seconds / self.SECONDS_PER_DAY
        elif unit == 'month' or unit == 'months':
            return seconds / self.SECONDS_PER_MONTH
        elif unit == 'year' or unit == 'years':
            return seconds / self.SECONDS_PER_YEAR
        else:
            raise ValueError(f"Unknown time unit: {unit}")

    def convert(self, value, from_unit, to_unit):
        seconds = self.to_seconds(value, from_unit)
        return self.from_seconds(seconds, to_unit)

if __name__ == '__main__':
    converter = TimeUnitConverter()
    print(converter.convert(1, 'year', 'seconds'))
    print(converter.convert(86400, 'seconds', 'days'))
    print(converter.convert(1, 'month', 'hours'))
    print(converter.convert(24, 'hours', 'minutes'))
    print(converter.convert(1, 'year', 'months'))
    print(converter.convert(365.25, 'days', 'years'))