class TimeConverter:
    SECONDS_IN_MINUTE = 60
    MINUTES_IN_HOUR = 60
    HOURS_IN_DAY = 24
    DAYS_IN_MONTH = 30.44
    DAYS_IN_YEAR = 365.24

    def to_seconds(self, value, unit):
        if unit == 'seconds':
            return value
        if unit == 'minutes':
            return value * self.SECONDS_IN_MINUTE
        if unit == 'hours':
            return value * self.SECONDS_IN_MINUTE * self.MINUTES_IN_HOUR
        if unit == 'days':
            return value * self.SECONDS_IN_MINUTE * self.MINUTES_IN_HOUR * self.HOURS_IN_DAY
        if unit == 'months':
            return value * self.SECONDS_IN_MINUTE * self.MINUTES_IN_HOUR * self.HOURS_IN_DAY * self.DAYS_IN_MONTH
        if unit == 'years':
            return value * self.SECONDS_IN_MINUTE * self.MINUTES_IN_HOUR * self.HOURS_IN_DAY * self.DAYS_IN_YEAR
        raise ValueError("Invalid unit provided")

    def from_seconds(self, value, unit):
        if unit == 'seconds':
            return value
        if unit == 'minutes':
            return value / self.SECONDS_IN_MINUTE
        if unit == 'hours':
            return value / (self.SECONDS_IN_MINUTE * self.MINUTES_IN_HOUR)
        if unit == 'days':
            return value / (self.SECONDS_IN_MINUTE * self.MINUTES_IN_HOUR * self.HOURS_IN_DAY)
        if unit == 'months':
            return value / (self.SECONDS_IN_MINUTE * self.MINUTES_IN_HOUR * self.HOURS_IN_DAY * self.DAYS_IN_MONTH)
        if unit == 'years':
            return value / (self.SECONDS_IN_MINUTE * self.MINUTES_IN_HOUR * self.HOURS_IN_DAY * self.DAYS_IN_YEAR)
        raise ValueError("Invalid unit provided")

    def convert(self, value, from_unit, to_unit):
        seconds = self.to_seconds(value, from_unit)
        return self.from_seconds(seconds, to_unit)

if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.convert(1, 'years', 'days'))
    print(converter.convert(60, 'minutes', 'seconds'))
    print(converter.convert(2, 'hours', 'minutes'))
    print(converter.convert(1, 'month', 'hours'))
    print(converter.convert(1000000, 'seconds', 'days'))
    print(converter.convert(50000, 'minutes', 'years'))
    print(converter.convert(365.24, 'days', 'years'))
    print(converter.convert(1, 'second', 'hours'))