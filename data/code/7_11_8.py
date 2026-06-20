class TimeConverter:
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    DAYS_PER_WEEK = 7

    @staticmethod
    def seconds_to_minutes(seconds):
        return seconds / TimeConverter.SECONDS_PER_MINUTE

    @staticmethod
    def seconds_to_hours(seconds):
        return seconds / (TimeConverter.SECONDS_PER_MINUTE * TimeConverter.MINUTES_PER_HOUR)

    @staticmethod
    def seconds_to_days(seconds):
        return seconds / (TimeConverter.SECONDS_PER_MINUTE * TimeConverter.MINUTES_PER_HOUR * TimeConverter.HOURS_PER_DAY)

    @staticmethod
    def minutes_to_hours(minutes):
        return minutes / TimeConverter.MINUTES_PER_HOUR

    @staticmethod
    def minutes_to_days(minutes):
        return minutes / (TimeConverter.MINUTES_PER_HOUR * TimeConverter.HOURS_PER_DAY)

    @staticmethod
    def hours_to_days(hours):
        return hours / TimeConverter.HOURS_PER_DAY

    @staticmethod
    def days_to_hours(days):
        return days * TimeConverter.HOURS_PER_DAY

    @staticmethod
    def days_to_seconds(days):
        return days * TimeConverter.HOURS_PER_DAY * TimeConverter.MINUTES_PER_HOUR * TimeConverter.SECONDS_PER_MINUTE

if __name__ == '__main__':
    converter = TimeConverter()
    seconds_input = 3600
    minutes_result = converter.seconds_to_minutes(seconds_input)
    hours_result = converter.seconds_to_hours(seconds_input)
    days_result = converter.seconds_to_days(86400)
    days_input = 2
    hours_from_days = converter.days_to_hours(days_input)
    print(minutes_result)
    print(hours_result)
    print(days_result)
    print(hours_from_days)