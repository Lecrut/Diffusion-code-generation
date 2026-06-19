class TimeConverter:
    def seconds_to_minutes(self, seconds):
        return seconds / 60

    def minutes_to_hours(self, minutes):
        return minutes / 60

    def hours_to_days(self, hours):
        return hours / 24

    def days_to_years(self, days):
        return days / 365.25

    def years_to_seconds(self, years):
        return years * 365.25 * 24 * 60 * 60

if __name__ == '__main__':
    converter = TimeConverter()
    
    seconds = 3600
    minutes = converter.seconds_to_minutes(seconds)
    hours = converter.minutes_to_hours(minutes)
    days = converter.hours_to_days(hours)
    years = converter.days_to_years(days)
    
    print(f"Seconds: {seconds}")
    print(f"Minutes: {minutes}")
    print(f"Hours: {hours}")
    print(f"Days: {days}")
    print(f"Years: {years}")