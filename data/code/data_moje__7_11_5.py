class TimeConverter:
    SECONDS_IN_MINUTE = 60
    MINUTES_IN_HOUR = 60
    HOURS_IN_DAY = 24
    DAYS_IN_WEEK = 7
    DAYS_IN_MONTH = 30
    DAYS_IN_YEAR = 365

    @staticmethod
    def seconds_to_minutes(seconds):
        if seconds < 0:
            raise ValueError("Time cannot be negative")
        return seconds / TimeConverter.SECONDS_IN_MINUTE

    @staticmethod
    def seconds_to_hours(seconds):
        if seconds < 0:
            raise ValueError("Time cannot be negative")
        minutes = TimeConverter.seconds_to_minutes(seconds)
        return minutes / TimeConverter.MINUTES_IN_HOUR

    @staticmethod
    def seconds_to_days(seconds):
        if seconds < 0:
            raise ValueError("Time cannot be negative")
        hours = TimeConverter.seconds_to_hours(seconds)
        return hours / TimeConverter.HOURS_IN_DAY

    @staticmethod
    def minutes_to_hours(minutes):
        if minutes < 0:
            raise ValueError("Time cannot be negative")
        return minutes / TimeConverter.MINUTES_IN_HOUR

    @staticmethod
    def minutes_to_days(minutes):
        if minutes < 0:
            raise ValueError("Time cannot be negative")
        hours = TimeConverter.minutes_to_hours(minutes)
        return hours / TimeConverter.HOURS_IN_DAY

    @staticmethod
    def hours_to_days(hours):
        if hours < 0:
            raise ValueError("Time cannot be negative")
        return hours / TimeConverter.HOURS_IN_DAY

    @staticmethod
    def days_to_weeks(days):
        if days < 0:
            raise ValueError("Time cannot be negative")
        return days / TimeConverter.DAYS_IN_WEEK

    @staticmethod
    def days_to_months(days):
        if days < 0:
            raise ValueError("Time cannot be negative")
        return days / TimeConverter.DAYS_IN_MONTH

    @staticmethod
    def days_to_years(days):
        if days < 0:
            raise ValueError("Time cannot be negative")
        return days / TimeConverter.DAYS_IN_YEAR

    @staticmethod
    def weeks_to_days(weeks):
        if weeks < 0:
            raise ValueError("Time cannot be negative")
        return weeks * TimeConverter.DAYS_IN_WEEK

    @staticmethod
    def months_to_days(months):
        if months < 0:
            raise ValueError("Time cannot be negative")
        return months * TimeConverter.DAYS_IN_MONTH

    @staticmethod
    def years_to_days(years):
        if years < 0:
            raise ValueError("Time cannot be negative")
        return years * TimeConverter.DAYS_IN_YEAR

if __name__ == '__main__':
    converter = TimeConverter()
    sample_seconds = 7200
    minutes_result = converter.seconds_to_minutes(sample_seconds)
    hours_result = converter.seconds_to_hours(sample_seconds)
    days_result = converter.seconds_to_days(sample_seconds)
    print(minutes_result)
    print(hours_result)
    print(days_result)
    sample_days = 105
    weeks_result = converter.days_to_weeks(sample_days)
    print(weeks_result)