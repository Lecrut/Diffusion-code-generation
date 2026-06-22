class TimeConverter:
    SECONDS_IN_MINUTE = 60
    MINUTES_IN_HOUR = 60
    HOURS_IN_DAY = 24
    DAYS_IN_YEAR = 365
    DAYS_IN_MONTH = 30

    @staticmethod
    def _to_seconds(value: float, unit: str) -> float:
        unit = unit.lower()
        if unit == 'second':
            return value
        if unit == 'minute':
            return value * TimeConverter.SECONDS_IN_MINUTE
        if unit == 'hour':
            return value * TimeConverter.SECONDS_IN_MINUTE * TimeConverter.MINUTES_IN_HOUR
        if unit == 'day':
            return value * TimeConverter.SECONDS_IN_MINUTE * TimeConverter.MINUTES_IN_HOUR * TimeConverter.HOURS_IN_DAY
        if unit == 'month':
            return value * TimeConverter.SECONDS_IN_MINUTE * TimeConverter.MINUTES_IN_HOUR * TimeConverter.HOURS_IN_DAY * TimeConverter.DAYS_IN_MONTH
        if unit == 'year':
            return value * TimeConverter.SECONDS_IN_MINUTE * TimeConverter.MINUTES_IN_HOUR * TimeConverter.HOURS_IN_DAY * TimeConverter.DAYS_IN_YEAR
        raise ValueError(f"Unknown unit: {unit}")

    @staticmethod
    def _from_seconds(seconds: float, target_unit: str) -> float:
        unit = target_unit.lower()
        if unit == 'second':
            return seconds
        if unit == 'minute':
            return seconds / TimeConverter.SECONDS_IN_MINUTE
        if unit == 'hour':
            return seconds / (TimeConverter.SECONDS_IN_MINUTE * TimeConverter.MINUTES_IN_HOUR)
        if unit == 'day':
            return seconds / (TimeConverter.SECONDS_IN_MINUTE * TimeConverter.MINUTES_IN_HOUR * TimeConverter.HOURS_IN_DAY)
        if unit == 'month':
            return seconds / (TimeConverter.SECONDS_IN_MINUTE * TimeConverter.MINUTES_IN_HOUR * TimeConverter.HOURS_IN_DAY * TimeConverter.DAYS_IN_MONTH)
        if unit == 'year':
            return seconds / (TimeConverter.SECONDS_IN_MINUTE * TimeConverter.MINUTES_IN_HOUR * TimeConverter.HOURS_IN_DAY * TimeConverter.DAYS_IN_YEAR)
        raise ValueError(f"Unknown unit: {target_unit}")

    @staticmethod
    def convert(value: float, from_unit: str, to_unit: str) -> float:
        seconds = TimeConverter._to_seconds(value, from_unit)
        return TimeConverter._from_seconds(seconds, to_unit)

if __name__ == '__main__':
    converter = TimeConverter()
    years_to_days = converter.convert(1.5, 'year', 'day')
    print(f"1.5 years in days: {years_to_days}")
    hours_to_minutes = converter.convert(2.5, 'hour', 'minute')
    print(f"2.5 hours in minutes: {hours_to_minutes}")
    months_to_seconds = converter.convert(3, 'month', 'second')
    print(f"3 months in seconds: {months_to_seconds}")
    days_to_hours = converter.convert(7, 'day', 'hour')
    print(f"7 days in hours: {days_to_hours}")
    minutes_to_days = converter.convert(1440, 'minute', 'day')
    print(f"1440 minutes in days: {minutes_to_days}")