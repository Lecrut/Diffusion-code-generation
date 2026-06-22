class TimeConverter:
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    DAYS_PER_WEEK = 7
    WEEKS_PER_YEAR = 52.1429

    def seconds_to_minutes(self, seconds):
        return seconds / self.SECONDS_PER_MINUTE

    def minutes_to_hours(self, minutes):
        return minutes / self.MINUTES_PER_HOUR

    def hours_to_days(self, hours):
        return hours / self.HOURS_PER_DAY

    def days_to_weeks(self, days):
        return days / self.DAYS_PER_WEEK

    def weeks_to_years(self, weeks):
        return weeks / self.WEEKS_PER_YEAR

if __name__ == '__main__':
    converter = TimeConverter()
    total_seconds = 86400
    minutes = converter.seconds_to_minutes(total_seconds)
    hours = converter.minutes_to_hours(minutes)
    days = converter.hours_to_days(hours)
    weeks = converter.days_to_weeks(days)
    years = converter.weeks_to_years(weeks)

    print(f"Total seconds: {total_seconds}")
    print(f"Converted to minutes: {minutes}")
    print(f"Converted to hours: {hours}")
    print(f"Converted to days: {days}")
    print(f"Converted to weeks: {weeks}")
    print(f"Converted to years: {years}")