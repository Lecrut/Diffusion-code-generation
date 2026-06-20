class TimeConverter:
    def hours_to_minutes(self, hours):
        return hours * 60

    def hours_to_seconds(self, hours):
        return hours * 3600

    def minutes_to_hours(self, minutes):
        return minutes / 60

    def minutes_to_seconds(self, minutes):
        return minutes * 60

    def seconds_to_hours(self, seconds):
        return seconds / 3600

    def seconds_to_minutes(self, seconds):
        return seconds / 60

if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.hours_to_minutes(2.5))
    print(converter.hours_to_seconds(1.5))
    print(converter.minutes_to_hours(90))
    print(converter.minutes_to_seconds(45))
    print(converter.seconds_to_hours(7200))
    print(converter.seconds_to_minutes(1800))