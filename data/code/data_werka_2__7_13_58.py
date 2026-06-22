class TimeConverter:
    HOURS_TO_SECONDS = 3600
    MINUTES_TO_SECONDS = 60

    @staticmethod
    def convert_to_seconds(hours, minutes, seconds):
        if hours < 0 or minutes < 0 or seconds < 0:
            raise ValueError("Time components must be non-negative")
        return (hours * TimeConverter.HOURS_TO_SECONDS +
                minutes * TimeConverter.MINUTES_TO_SECONDS +
                seconds)

if __name__ == '__main__':
    sample_hours = 1
    sample_minutes = 30
    sample_seconds = 45
    converter = TimeConverter()
    total_seconds = converter.convert_to_seconds(sample_hours, sample_minutes, sample_seconds)
    print(total_seconds)