class TimeConverter:
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24

    def __init__(self, total_seconds):
        self.total_seconds = total_seconds

    def convert_to_dhms(self):
        days = self.total_seconds // (self.SECONDS_PER_MINUTE * self.MINUTES_PER_HOUR * self.HOURS_PER_DAY)
        hours = (self.total_seconds % (self.SECONDS_PER_MINUTE * self.MINUTES_PER_HOUR * self.HOURS_PER_DAY)) // (self.SECONDS_PER_MINUTE * self.MINUTES_PER_HOUR)
        minutes = (self.total_seconds % (self.SECONDS_PER_MINUTE * self.MINUTES_PER_HOUR)) // self.SECONDS_PER_MINUTE
        seconds = self.total_seconds % self.SECONDS_PER_MINUTE
        return days, hours, minutes, seconds

if __name__ == '__main__':
    sample_duration = 1234567
    converter = TimeConverter(sample_duration)
    days, hours, minutes, seconds = converter.convert_to_dhms()
    print(f"{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds")