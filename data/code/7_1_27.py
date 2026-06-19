class TimeConverter:

    def hours_to_minutes(self, hours):
        return hours * 60

    def minutes_to_seconds(self, minutes):
        return minutes * 60

    def seconds_to_hours(self, seconds):
        return seconds / 3600

    def seconds_to_minutes(self, seconds):
        return seconds / 60
if __name__ == '__main__':
    converter = TimeConverter()
    hours = 5
    minutes = 45
    seconds = 1200
    print(converter.hours_to_minutes(hours))
    print(converter.minutes_to_seconds(minutes))
    print(converter.seconds_to_hours(seconds))
    print(converter.seconds_to_minutes(seconds))