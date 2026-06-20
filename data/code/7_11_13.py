class TimeConverter:
    SECONDS_IN_MINUTE = 60
    MINUTES_IN_HOUR = 60
    HOURS_IN_DAY = 24
    DAYS_IN_WEEK = 7
    DAYS_IN_MONTH = 30.44
    DAYS_IN_YEAR = 365.25

    @staticmethod
    def seconds_to_minutes(seconds):
        return seconds / TimeConverter.SECONDS_IN_MINUTE

    @staticmethod
    def seconds_to_hours(seconds):
        return seconds / (TimeConverter.SECONDS_IN_MINUTE * TimeConverter.MINUTES_IN_HOUR)

    @staticmethod
    def seconds_to_days(seconds):
        return seconds / (TimeConverter.SECONDS_IN_MINUTE * TimeConverter.MINUTES_IN_HOUR * TimeConverter.HOURS_IN_DAY)

    @staticmethod
    def minutes_to_hours(minutes):
        return minutes / TimeConverter.MINUTES_IN_HOUR

    @staticmethod
    def minutes_to_days(minutes):
        return minutes / (TimeConverter.MINUTES_IN_HOUR * TimeConverter.HOURS_IN_DAY)

    @staticmethod
    def hours_to_days(hours):
        return hours / TimeConverter.HOURS_IN_DAY

    @staticmethod
    def hours_to_weeks(hours):
        return hours / (TimeConverter.HOURS_IN_DAY * TimeConverter.DAYS_IN_WEEK)

    @staticmethod
    def days_to_weeks(days):
        return days / TimeConverter.DAYS_IN_WEEK

    @staticmethod
    def days_to_months(days):
        return days / TimeConverter.DAYS_IN_MONTH

    @staticmethod
    def days_to_years(days):
        return days / TimeConverter.DAYS_IN_YEAR

    @staticmethod
    def convert(value, from_unit, to_unit):
        conversion_map = {
            ('seconds', 'minutes'): lambda x: x / TimeConverter.SECONDS_IN_MINUTE,
            ('seconds', 'hours'): lambda x: x / (TimeConverter.SECONDS_IN_MINUTE * TimeConverter.MINUTES_IN_HOUR),
            ('seconds', 'days'): lambda x: x / (TimeConverter.SECONDS_IN_MINUTE * TimeConverter.MINUTES_IN_HOUR * TimeConverter.HOURS_IN_DAY),
            ('minutes', 'seconds'): lambda x: x * TimeConverter.SECONDS_IN_MINUTE,
            ('minutes', 'hours'): lambda x: x / TimeConverter.MINUTES_IN_HOUR,
            ('minutes', 'days'): lambda x: x / (TimeConverter.MINUTES_IN_HOUR * TimeConverter.HOURS_IN_DAY),
            ('hours', 'minutes'): lambda x: x * TimeConverter.MINUTES_IN_HOUR,
            ('hours', 'seconds'): lambda x: x * TimeConverter.SECONDS_IN_MINUTE * TimeConverter.MINUTES_IN_HOUR,
            ('hours', 'days'): lambda x: x / TimeConverter.HOURS_IN_DAY,
            ('days', 'hours'): lambda x: x * TimeConverter.HOURS_IN_DAY,
            ('days', 'minutes'): lambda x: x * TimeConverter.HOURS_IN_DAY * TimeConverter.MINUTES_IN_HOUR,
            ('days', 'seconds'): lambda x: x * TimeConverter.HOURS_IN_DAY * TimeConverter.MINUTES_IN_HOUR * TimeConverter.SECONDS_IN_MINUTE,
            ('days', 'weeks'): lambda x: x / TimeConverter.DAYS_IN_WEEK,
            ('weeks', 'days'): lambda x: x * TimeConverter.DAYS_IN_WEEK,
            ('days', 'months'): lambda x: x / TimeConverter.DAYS_IN_MONTH,
            ('months', 'days'): lambda x: x * TimeConverter.DAYS_IN_MONTH,
            ('days', 'years'): lambda x: x / TimeConverter.DAYS_IN_YEAR,
            ('years', 'days'): lambda x: x * TimeConverter.DAYS_IN_YEAR,
        }
        key = (from_unit, to_unit)
        if key in conversion_map:
            return conversion_map[key](value)
        raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")

if __name__ == '__main__':
    converter = TimeConverter()
    result1 = converter.seconds_to_minutes(300)
    print(result1)
    result2 = TimeConverter.convert(1, 'hours', 'seconds')
    print(result2)
    result3 = converter.days_to_years(730)
    print(result3)