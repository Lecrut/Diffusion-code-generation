class TimeConverter:
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    DAYS_PER_WEEK = 7
    WEEKS_PER_YEAR = 52.1429
    YEARS_PER_DECADE = 10
    DECADES_PER_CENTURY = 10

    def _validate_positive(self, value):
        if value < 0:
            raise ValueError("Time units must be non-negative")

    def seconds_to_minutes(self, seconds):
        self._validate_positive(seconds)
        return seconds / self.SECONDS_PER_MINUTE

    def minutes_to_hours(self, minutes):
        self._validate_positive(minutes)
        return minutes / self.MINUTES_PER_HOUR

    def hours_to_days(self, hours):
        self._validate_positive(hours)
        return hours / self.HOURS_PER_DAY

    def days_to_weeks(self, days):
        self._validate_positive(days)
        return days / self.DAYS_PER_WEEK

    def weeks_to_years(self, weeks):
        self._validate_positive(weeks)
        return weeks / self.WEEKS_PER_YEAR

    def years_to_decades(self, years):
        self._validate_positive(years)
        return years / self.YEARS_PER_DECADE

    def decades_to_centuries(self, decades):
        self._validate_positive(decades)
        return decades / self.DECADES_PER_CENTURY

if __name__ == '__main__':
    converter = TimeConverter()
    seconds = 3600
    minutes = converter.seconds_to_minutes(seconds)
    hours = converter.minutes_to_hours(minutes)
    days = converter.hours_to_days(hours)
    weeks = converter.days_to_weeks(days)
    years = converter.weeks_to_years(weeks)

    print(f"Seconds: {seconds}")
    print(f"Minutes: {minutes}")
    print(f"Hours: {hours}")
    print(f"Days: {days}")
    print(f"Weeks: {weeks}")
    print(f"Years: {years}")