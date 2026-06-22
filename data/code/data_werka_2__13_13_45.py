class TimeConverter:
    SECONDS_IN_DAY = 86400
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_MINUTE = 60

    def __init__(self, total_seconds):
        if not isinstance(total_seconds, int) or total_seconds < 0:
            raise ValueError("Total seconds must be a non-negative integer.")
        self.total_seconds = total_seconds

    def convert_to_dhms(self):
        days = self.total_seconds // self.SECONDS_IN_DAY
        hours = (self.total_seconds % self.SECONDS_IN_DAY) // self.SECONDS_IN_HOUR
        minutes = (self.total_seconds % self.SECONDS_IN_HOUR) // self.SECONDS_IN_MINUTE
        seconds = self.total_seconds % self.SECONDS_IN_MINUTE
        return days, hours, minutes, seconds

if __name__ == '__main__':
    sample_duration = 1234567
    converter = TimeConverter(sample_duration)
    days, hours, minutes, seconds = converter.convert_to_dhms()
    print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")