class TimeConverter:
    HOURS_TO_SECONDS = 3600
    MINUTES_TO_SECONDS = 60

    @staticmethod
    def convert_to_seconds(hours, minutes, seconds):
        if hours < 0 or minutes < 0 or seconds < 0:
            raise ValueError("Time components must be non-negative")
        total_seconds = (hours * TimeConverter.HOURS_TO_SECONDS +
                         minutes * TimeConverter.MINUTES_TO_SECONDS +
                         seconds)
        return total_seconds

if __name__ == '__main__':
    converter = TimeConverter()
    sample_hours = 4
    sample_minutes = 30
    sample_seconds = 10
    total_seconds = converter.convert_to_seconds(sample_hours, sample_minutes, sample_seconds)
    print(total_seconds)