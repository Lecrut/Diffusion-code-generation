class TimeConverter:
    def seconds_to_minutes(self, seconds):
        return seconds / 60.0
    def minutes_to_hours(self, minutes):
        return minutes / 60.0
    def hours_to_days(self, hours):
        return hours / 24.0
    def days_to_hours(self, days):
        return days * 24.0
if __name__ == '__main__':
    converter = TimeConverter()
    seconds = 3661
    minutes = 135
    hours = 72
    days = 3.5
    print(f"Converting {seconds} seconds to minutes: {converter.seconds_to_minutes(seconds)}")
    print(f"Converting {minutes} minutes to hours: {converter.minutes_to_hours(minutes)}")
    print(f"Converting {hours} hours to days: {converter.hours_to_days(hours)}")
    print(f"Converting {days} days to hours: {converter.days_to_hours(days)}")