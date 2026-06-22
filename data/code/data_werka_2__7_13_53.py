class TimeConverter:
    HOURS_TO_SECONDS = 3600
    MINUTES_TO_SECONDS = 60

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def convert_to_seconds(self):
        total_seconds = (self.hours * self.HOURS_TO_SECONDS +
                         self.minutes * self.MINUTES_TO_SECONDS +
                         self.seconds)
        return total_seconds

if __name__ == '__main__':
    converter1 = TimeConverter(hours=2, minutes=45, seconds=30)
    print(converter1.convert_to_seconds())

    converter2 = TimeConverter(hours=3, minutes=15, seconds=45)
    print(converter2.convert_to_seconds())