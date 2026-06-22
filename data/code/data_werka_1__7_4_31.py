class TimeUnitConverter:
    SECONDS_IN_MINUTE = 60
    MINUTES_IN_HOUR = 60
    HOURS_IN_DAY = 24
    DAYS_IN_WEEK = 7
    WEEKS_IN_MONTH = 4.345
    MONTHS_IN_YEAR = 12

    def seconds_to_minutes(self, seconds):
        return seconds / self.SECONDS_IN_MINUTE

    def minutes_to_hours(self, minutes):
        return minutes / self.MINUTES_IN_HOUR

    def hours_to_days(self, hours):
        return hours / self.HOURS_IN_DAY

    def days_to_weeks(self, days):
        return days / self.DAYS_IN_WEEK

    def weeks_to_months(self, weeks):
        return weeks / self.WEEKS_IN_MONTH

    def months_to_years(self, months):
        return months / self.MONTHS_IN_YEAR

    def years_to_months(self, years):
        return years * self.MONTHS_IN_YEAR

    def months_to_weeks(self, months):
        return months * self.WEEKS_IN_MONTH

    def weeks_to_days(self, weeks):
        return weeks * self.DAYS_IN_WEEK

    def days_to_hours(self, days):
        return days * self.HOURS_IN_DAY

    def hours_to_minutes(self, hours):
        return hours * self.MINUTES_IN_HOUR

    def minutes_to_seconds(self, minutes):
        return minutes * self.SECONDS_IN_MINUTE
if __name__ == '__main__':
    converter = TimeUnitConverter()
    print(converter.seconds_to_minutes(3600))
    print(converter.minutes_to_hours(120))
    print(converter.hours_to_days(24))
    print(converter.days_to_weeks(7))
    print(converter.weeks_to_months(4))
    print(converter.months_to_years(12))
    print(converter.years_to_months(5))
    print(converter.months_to_weeks(3))
    print(converter.weeks_to_days(8))
    print(converter.days_to_hours(10))
    print(converter.hours_to_minutes(60))
    print(converter.minutes_to_seconds(45))