class TimeConverter:
    SECONDS_IN_MINUTE = 60
    MINUTES_IN_HOUR = 60
    HOURS_IN_DAY = 24

    def __init__(self, days=0, hours=0, minutes=0, seconds=0):
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def total_minutes(self):
        total_seconds = (self.days * self.HOURS_IN_DAY * self.MINUTES_IN_HOUR * self.SECONDS_IN_MINUTE) + \
                       (self.hours * self.MINUTES_IN_HOUR * self.SECONDS_IN_MINUTE) + \
                       (self.minutes * self.SECONDS_IN_MINUTE) + \
                       self.seconds
        return total_seconds // self.SECONDS_IN_MINUTE

if __name__ == '__main__':
    converter = TimeConverter(days=1, hours=6, minutes=45, seconds=30)
    print(converter.total_minutes())