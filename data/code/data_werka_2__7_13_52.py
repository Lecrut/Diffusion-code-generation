class TimeConverter:
    HOURS_TO_SECONDS = 3600
    MINUTES_TO_SECONDS = 60

    def convert_to_seconds(self, hours, minutes, seconds):
        if not all(isinstance(x, int) and x >= 0 for x in (hours, minutes, seconds)):
            raise ValueError("Time components must be non-negative integers")
        
        total_seconds = (
            hours * self.HOURS_TO_SECONDS +
            minutes * self.MINUTES_TO_SECONDS +
            seconds
        )
        return total_seconds

if __name__ == '__main__':
    converter = TimeConverter()
    sample_hours = 4
    sample_minutes = 30
    sample_seconds = 10
    total_seconds = converter.convert_to_seconds(sample_hours, sample_minutes, sample_seconds)
    print(total_seconds)