class TimeConverter:
    HOURS_TO_SECONDS = 3600
    MINUTES_TO_SECONDS = 60

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self._validate_time()

    def _validate_time(self):
        if self.hours < 0 or self.minutes < 0 or self.seconds < 0:
            raise ValueError("Time components must be non-negative")
        if self.minutes >= 60 or self.seconds >= 60:
            raise ValueError("Minutes and seconds must be less than 60")

    def convert_to_seconds(self):
        return (self.hours * TimeConverter.HOURS_TO_SECONDS +
                self.minutes * TimeConverter.MINUTES_TO_SECONDS +
                self.seconds)

if __name__ == '__main__':
    sample_hours = 4
    sample_minutes = 59
    sample_seconds = 58
    converter = TimeConverter(sample_hours, sample_minutes, sample_seconds)
    total_seconds = converter.convert_to_seconds()
    print(total_seconds)