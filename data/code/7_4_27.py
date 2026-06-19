class TimeUnitConverter:

    def __init__(self):
        self.seconds_per_minute = 60
        self.minutes_per_hour = 60
        self.hours_per_day = 24
        self.days_per_month = 30.44
        self.months_per_year = 12

    def seconds_to_minutes(self, seconds):
        return seconds / self.seconds_per_minute

    def minutes_to_hours(self, minutes):
        return minutes / self.minutes_per_hour

    def hours_to_days(self, hours):
        return hours / self.hours_per_day

    def days_to_months(self, days):
        return days / self.days_per_month

    def months_to_years(self, months):
        return months / self.months_per_year

    def years_to_months(self, years):
        return years * self.months_per_year

    def months_to_days(self, months):
        return months * self.days_per_month

    def days_to_hours(self, days):
        return days * self.hours_per_day

    def hours_to_minutes(self, hours):
        return hours * self.minutes_per_hour

    def minutes_to_seconds(self, minutes):
        return minutes * self.seconds_per_minute
if __name__ == '__main__':
    converter = TimeUnitConverter()
    print(converter.seconds_to_minutes(3600))
    print(converter.minutes_to_hours(120))
    print(converter.hours_to_days(48))
    print(converter.days_to_months(365))
    print(converter.months_to_years(144))
    print(converter.years_to_months(5))
    print(converter.months_to_days(72))
    print(converter.days_to_hours(365))
    print(converter.hours_to_minutes(1440))
    print(converter.minutes_to_seconds(60))