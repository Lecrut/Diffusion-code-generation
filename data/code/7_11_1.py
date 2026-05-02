class TimeConverter:
    def __init__(self):
        pass
    def seconds_to_minutes(self, seconds):
        return seconds / 60.0
    def minutes_to_seconds(self, minutes):
        return minutes * 60.0
    def minutes_to_hours(self, minutes):
        return minutes / 60.0
    def hours_to_minutes(self, hours):
        return hours * 60.0
    def hours_to_days(self, hours):
        return hours / 24.0
    def days_to_hours(self, days):
        return days * 24.0
if __name__ == '__main__':
    converter = TimeConverter()
    sample_seconds = 3600
    sample_minutes = 120
    sample_hours = 24
    sample_days = 7
    print(f"Converting {sample_seconds} seconds to minutes: {converter.seconds_to_minutes(sample_seconds)}")
    print(f"Converting {sample_minutes} minutes to seconds: {converter.minutes_to_seconds(sample_minutes)}")
    print(f"Converting {sample_minutes} minutes to hours: {converter.minutes_to_hours(sample_minutes)}")
    print(f"Converting {sample_hours} hours to minutes: {converter.hours_to_minutes(sample_hours)}")
    print(f"Converting {sample_hours} hours to days: {converter.hours_to_days(sample_hours)}")
    print(f"Converting {sample_days} days to hours: {converter.days_to_hours(sample_days)}")