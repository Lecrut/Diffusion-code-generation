class TimeConverter:

    def seconds_to_minutes(self, seconds):
        return seconds / 60

    def minutes_to_hours(self, minutes):
        return minutes / 60

    def hours_to_days(self, hours):
        return hours / 24

    def days_to_years(self, days):
        return days / 365.25
if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.seconds_to_minutes(120))
    print(converter.minutes_to_hours(60))
    print(converter.hours_to_days(24))
    print(converter.days_to_years(365))