class TimeConverter:

    def seconds_to_minutes(self, seconds):
        return seconds / 60

    def minutes_to_hours(self, minutes):
        return minutes / 60

    def hours_to_days(self, hours):
        return hours / 24

    def days_to_weeks(self, days):
        return days / 7

    def weeks_to_years(self, weeks):
        return weeks / 52.1429
if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.seconds_to_minutes(3600))
    print(converter.minutes_to_hours(120))
    print(converter.hours_to_days(48))
    print(converter.days_to_weeks(7))
    print(converter.weeks_to_years(52))