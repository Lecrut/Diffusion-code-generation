class TimeConverter:
    SECONDS_IN_MINUTE = 60
    MINUTES_IN_HOUR = 60
    HOURS_IN_DAY = 24
    DAYS_IN_WEEK = 7
    WEEKS_IN_MONTH_APPROX = 4.345
    MONTHS_IN_YEAR_APPROX = 12
    SECONDS_IN_HOUR = SECONDS_IN_MINUTE * MINUTES_IN_HOUR
    SECONDS_IN_DAY = SECONDS_IN_HOUR * HOURS_IN_DAY

    @staticmethod
    def seconds_to_minutes(seconds):
        return seconds / TimeConverter.SECONDS_IN_MINUTE

    @staticmethod
    def seconds_to_hours(seconds):
        return seconds / TimeConverter.SECONDS_IN_HOUR

    @staticmethod
    def seconds_to_days(seconds):
        return seconds / TimeConverter.SECONDS_IN_DAY

    @staticmethod
    def minutes_to_hours(minutes):
        return minutes / TimeConverter.MINUTES_IN_HOUR

    @staticmethod
    def minutes_to_days(minutes):
        return minutes / TimeConverter.SECONDS_IN_DAY * TimeConverter.SECONDS_IN_MINUTE

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
        return days / (TimeConverter.DAYS_IN_WEEK * TimeConverter.WEEKS_IN_MONTH_APPROX)

    @staticmethod
    def weeks_to_days(weeks):
        return weeks * TimeConverter.DAYS_IN_WEEK

    @staticmethod
    def months_to_days(months):
        return months * TimeConverter.DAYS_IN_WEEK * TimeConverter.WEEKS_IN_MONTH_APPROX

if __name__ == '__main__':
    converter = TimeConverter()
    sample_seconds = 3661
    result_minutes = converter.seconds_to_minutes(sample_seconds)
    result_hours = converter.seconds_to_hours(sample_seconds)
    result_days = converter.seconds_to_days(168)
    result_weeks = converter.hours_to_weeks(168)
    result_days_from_months = converter.months_to_days(2.5)
    print(result_minutes)
    print(result_hours)
    print(result_days)
    print(result_weeks)
    print(result_days_from_months)