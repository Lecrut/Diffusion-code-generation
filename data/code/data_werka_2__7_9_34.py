class TimeConverter:
    SECONDS_IN_MINUTE = 60
    MINUTES_IN_HOUR = 60
    HOURS_IN_DAY = 24
    DAYS_IN_WEEK = 7
    WEEKS_IN_YEAR = 52.1429

    def seconds_to_minutes(self, seconds):
        return seconds / self.SECONDS_IN_MINUTE

    def minutes_to_hours(self, minutes):
        return minutes / self.MINUTES_IN_HOUR

    def hours_to_days(self, hours):
        return hours / self.HOURS_IN_DAY

    def days_to_weeks(self, days):
        return days / self.DAYS_IN_WEEK

    def weeks_to_years(self, weeks):
        return weeks / self.WEEKS_IN_YEAR

if __name__ == '__main__':
    converter = TimeConverter()
    seconds = 3600
    minutes = converter.seconds_to_minutes(seconds)
    hours = converter.minutes_to_hours(minutes)
    days = converter.hours_to_days(hours)
    weeks = converter.days_to_weeks(days)
    years = converter.weeks_to_years(weeks)

    print(f"Seconds: {seconds} -> Minutes: {minutes}")
    print(f"Minutes: {minutes} -> Hours: {hours}")
    print(f"Hours: {hours} -> Days: {days}")
    print(f"Days: {days} -> Weeks: {weeks}")
    print(f"Weeks: {weeks} -> Years: {years}")