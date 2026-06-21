class DurationConverter:
    SECONDS_PER_DAY = 3600 * 24
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60

    def __init__(self, total_seconds):
        self.total_seconds = total_seconds

    def convert(self):
        days = self.total_seconds // self.SECONDS_PER_DAY
        hours = (self.total_seconds % self.SECONDS_PER_DAY) // self.SECONDS_PER_HOUR
        minutes = (self.total_seconds % self.SECONDS_PER_HOUR) // self.SECONDS_PER_MINUTE
        remaining_seconds = self.total_seconds % self.SECONDS_PER_MINUTE
        return days, hours, minutes, remaining_seconds

if __name__ == '__main__':
    sample_values = [86401, 3662, 7201, 3601, 61, 1]
    for value in sample_values:
        converter = DurationConverter(value)
        print(converter.convert())