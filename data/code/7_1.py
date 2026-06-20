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
    sample_hours = 2.5
    sample_minutes = 45
    sample_seconds = 1800
    
    print(converter.hours_to_minutes(sample_hours))
    print(converter.hours_to_seconds(sample_hours))
    print(converter.minutes_to_hours(sample_minutes))
    print(converter.minutes_to_seconds(sample_minutes))
    print(converter.seconds_to_hours(sample_seconds))
    print(converter.seconds_to_minutes(sample_seconds))