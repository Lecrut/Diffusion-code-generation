class TimeUnitConverter:
    SECONDS_IN_MINUTE = 60
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_DAY = 86400
    SECONDS_IN_MONTH = 2629746
    SECONDS_IN_YEAR = 31556952

    @staticmethod
    def _to_seconds(value, unit):
        unit_lower = unit.lower()
        if unit_lower in ('s', 'second', 'seconds'):
            return float(value)
        elif unit_lower in ('min', 'minute', 'minutes'):
            return float(value) * TimeUnitConverter.SECONDS_IN_MINUTE
        elif unit_lower in ('h', 'hour', 'hours'):
            return float(value) * TimeUnitConverter.SECONDS_IN_HOUR
        elif unit_lower in ('d', 'day', 'days'):
            return float(value) * TimeUnitConverter.SECONDS_IN_DAY
        elif unit_lower in ('mo', 'month', 'months'):
            return float(value) * TimeUnitConverter.SECONDS_IN_MONTH
        elif unit_lower in ('y', 'year', 'years'):
            return float(value) * TimeUnitConverter.SECONDS_IN_YEAR
        else:
            raise ValueError(f"Invalid time unit: {unit}")

    @staticmethod
    def _from_seconds(total_seconds, unit):
        unit_lower = unit.lower()
        if unit_lower in ('s', 'second', 'seconds'):
            return total_seconds
        elif unit_lower in ('min', 'minute', 'minutes'):
            return total_seconds / TimeUnitConverter.SECONDS_IN_MINUTE
        elif unit_lower in ('h', 'hour', 'hours'):
            return total_seconds / TimeUnitConverter.SECONDS_IN_HOUR
        elif unit_lower in ('d', 'day', 'days'):
            return total_seconds / TimeUnitConverter.SECONDS_IN_DAY
        elif unit_lower in ('mo', 'month', 'months'):
            return total_seconds / TimeUnitConverter.SECONDS_IN_MONTH
        elif unit_lower in ('y', 'year', 'years'):
            return total_seconds / TimeUnitConverter.SECONDS_IN_YEAR
        else:
            raise ValueError(f"Invalid time unit: {unit}")

    @staticmethod
    def convert(value, from_unit, to_unit):
        seconds = TimeUnitConverter._to_seconds(value, from_unit)
        return TimeUnitConverter._from_seconds(seconds, to_unit)

if __name__ == '__main__':
    years = 2
    years_to_seconds = TimeUnitConverter.convert(years, 'years', 'seconds')
    print(f"{years} years is {years_to_seconds} seconds")

    seconds = 90
    seconds_to_minutes = TimeUnitConverter.convert(seconds, 'seconds', 'minutes')
    print(f"{seconds} seconds is {seconds_to_minutes} minutes")

    days = 365
    days_to_years = TimeUnitConverter.convert(days, 'days', 'years')
    print(f"{days} days is approximately {days_to_years} years")

    months = 15
    months_to_days = TimeUnitConverter.convert(months, 'months', 'days')
    print(f"{months} months is approximately {months_to_days} days")

    hours = 24.5
    hours_to_seconds = TimeUnitConverter.convert(hours, 'hours', 'seconds')
    print(f"{hours} hours is {hours_to_seconds} seconds")

    minutes = 1.5
    minutes_to_seconds = TimeUnitConverter.convert(minutes, 'minutes', 'seconds')
    print(f"{minutes} minutes is {minutes_to_seconds} seconds")