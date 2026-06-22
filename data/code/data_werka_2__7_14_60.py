class TimeConverter:
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24

    @staticmethod
    def convert_to_minutes(days=0, hours=0, minutes=0, seconds=0):
        total_seconds = (days * TimeConverter.HOURS_PER_DAY * 
                        TimeConverter.MINUTES_PER_HOUR * 
                        TimeConverter.SECONDS_PER_MINUTE) + \
                       (hours * TimeConverter.MINUTES_PER_HOUR * 
                        TimeConverter.SECONDS_PER_MINUTE) + \
                       (minutes * TimeConverter.SECONDS_PER_MINUTE) + seconds
        return total_seconds // TimeConverter.SECONDS_PER_MINUTE

if __name__ == '__main__':
    sample_days = 2
    sample_hours = 3
    sample_minutes = 15
    sample_seconds = 30
    result = TimeConverter.convert_to_minutes(sample_days, sample_hours, sample_minutes, sample_seconds)
    print(result)