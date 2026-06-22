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

    def years_to_decades(self, years):
        return years / 10

    def decades_to_centuries(self, decades):
        return decades / 10
if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.seconds_to_minutes(3600))
    print(converter.minutes_to_hours(1440))
    print(converter.hours_to_days(72))
    print(converter.days_to_weeks(365))
    print(converter.weeks_to_years(52))
    print(converter.years_to_decades(100))
    print(converter.decades_to_centuries(10))