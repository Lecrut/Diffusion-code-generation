class TimeConverter:
    def hours_to_minutes(self, hours):
        return hours * 60

    def minutes_to_seconds(self, minutes):
        return minutes * 60

    def seconds_to_hours(self, seconds):
        return seconds / 3600

    def seconds_to_minutes(self, seconds):
        return seconds / 60

    def minutes_to_hours(self, minutes):
        return minutes / 60

if __name__ == '__main__':
    converter = TimeConverter()
    
    hours = 2
    minutes = 150
    seconds = 9000
    
    print(f"{hours} hours to minutes: {converter.hours_to_minutes(hours)}")
    print(f"{minutes} minutes to seconds: {converter.minutes_to_seconds(minutes)}")
    print(f"{seconds} seconds to hours: {converter.seconds_to_hours(seconds)}")
    print(f"{seconds} seconds to minutes: {converter.seconds_to_minutes(seconds)}")
    print(f"{minutes} minutes to hours: {converter.minutes_to_hours(minutes)}")